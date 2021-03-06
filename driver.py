#!/usr/bin/python
"""
This application is intended to run on RaspberryPi startup and requires no console input
The application has four states, an initialization state, a location reader state, a wristband scanner state, and a wristband registration state
In this application, interrupts are triggered by button presses according to the attached schematic

Initialization State:
	All global variables are initialized
	Location is read from location file if one exists
	All imports are made
	All interrupts are registered

Event Scanning State:
	Scan wristband
	If new scan, continue, else, repeat
	Relay scan location, time, and wristband id to redis server
	Receive response from redis server
	Display data from redis response to LCD
	repeat

Location Reading State:
	Scan wristband
	If new scan, continue, else repeat
	Authenticate with wristband
	Read sectors to get location from wristband
	Update location file
	repeat

Registration Scanning State:
	Get user PIN
	Query redis server to receive Name & Shirt Size
	Display data from redis server
	Scan wristband
	Post wristband ID to redis with PIN
	Verify acknowledgment from redis
	repeat

FSM Diagram:
   +----------------+
   |                |
   | Initialization |
   |                |
   +-------+--------+
           |
           | Initialization Complete
           |
   +-------v--------+                            +------------------+
   |                |  Location Interrupt Fired  |                  |
   | Event Scanning +----------------------------> Location Reading |
   |                <----------------------------+                  |
   +------^---------+  Event Interrupt Fired     +----------------^-+
Event     || Registration Interrupt Fired        |                |
Interrupt ||                                     |                |
Fired     ||        Registration Interrupt Fired |                |
   +-------v---------------+                     |                |
   |                       <---------------------+                |
   | Registration Scanning |                                      |
   |                       +--------------------------------------+
   +-----------------------+        Location Interrupt Fired

"""

import time
import calendar
import threading
import logging

try:
	import RPi.GPIO as GPIO
except ImportError:
	logging.ERROR('RaspberryPi GPIO is unavailable; please check OS installation')
	exit(-1)

#TODO: import all HackPSU abstraction modules
#import hackpsuLCD as lcd
import HackPSUrfid as rfid
import HackPSUkeypad
import HackPSUredis as redis
import HackPSUconfig as config
import HackPSUlcd as lcd
	
global state 
state = 1

def getWifi():
	return "XXX%"
		
def advanceState(dummy):
	global state
	state = (state + 1)%3
	print("STATE " + str(state))

#Prevent warnings from reusing IO ports
GPIO.setwarnings(False)

#TODO
#Change to logging.WARNING or ERROR for release
logging.basicConfig(filename='scanner.log', level=logging.DEBUG)
	
#TODO
#register mode switch interrupts
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set GPIO25 as input (button)  
GPIO.add_event_detect(13, GPIO.RISING, callback=advanceState)

#TODO
#Load information from config file

#Launch into the scanner mode
configurationDictionary = config.getProperties("pi.cfg")
keypad = HackPSUkeypad.HackPSUkeypad()
	
lastUID = None
while True:
	if state == 0:
		print("Scanner mode")
		lcd.printDebug(configurationDictionary["location"], getWifi())
		#Wait until band is detected
		uid = None
		#Wait for a wristband
		while not rfid.detectBand():
			pass
		#Once we have one, go
		#If it stops here, restart the program
		lcd.printMsg("Scanning...")
		#Get UID, skip scan if same as last
		uid = rfid.getUID()
		#Pls no let multiple scans happen 
		if uid == lastUID:
			continue
		print(uid)
		lcd.printMsg("Scanned Wristband")
		#Tell redis who scanned, when, and where
		timestamp = calendar.timegm(time.gmtime())
		location = configurationDictionary["location"]
		result = redis.postScan(configurationDictionary["redisLocation"], uid, timestamp, location)
		lcd.printScan(result)
		lastUID = uid
	elif state == 1:
		print("Registration mode")
		lcd.printDebug(configurationDictionary["location"], getWifi())
		uid = None
		lcd.printMsg("Enter Pin")
		pin = keypad.getPin()
		lcd.printMsg("#=Sub, *=Clear")
		(name, size) = redis.postPin(configurationDictionary["redisLocation"], pin)
		lcd.printName(name)
		#lcd.printMsg("#=Sub, *=Clear")
		key = None
		while not (key == "#" or key == "*"):
			key = keypad.getKey()
			
		if key == "*":
			continue
		
		lcd.printDebug(configurationDictionary["location"], getWifi())
		lcd.printSize(size)
		
		while not rfid.detectBand():
			pass
		lcd.printMsg("Scanned")
		uid = rfid.getUID()
		resp = redis.postRegistration(configurationDictionary["redisLocation"], uid, pin)
		lcd.printRegistered(resp)
		time.sleep(1)
		lastUID = uid
	else:
		print("Location Mode")
		lcd.printDebug(configurationDictionary["location"], getWifi())
		uid = None
		lcd.printMsg("Waiting...")
		while not rfid.detectBand():
			pass
		lcd.printMsg("Detected Wristband")
		loc = rfid.readLocation()
		configurationDictionary["location"] = loc
		lcd.printLocation(loc)
		lastUID = uid
		config.setProperties("pi.cfg", configurationDictionary)
