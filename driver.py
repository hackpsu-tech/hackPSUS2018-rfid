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
import threaing
import logging

try:
	import RPi.GPIO as GPIO
except ImportError:
	logging.ERROR('RaspberryPi GPIO is unavailable; please check OS installation')
	exit(-1)

#TODO: import all HackPSU abstraction modules
#import hackpsuLCD as lcd
import hackpsuRFID as rfid
#import hackpsuKEYPAD as keypad
import hackpsuREDIS as redis
import hackpsuCONFIG as config

configurationDictionary = {"location":""}
	
#Funtion definitions for states (goto <lineNum> for init code)
def launchScanner():
	lastUID = None
	while True:
		#Wait until band is detected
		uid = None
		print("Waiting for scan")
		while not rfid.detectBand()):
			pass
		print("Scanning")
		#Get UID, skip scan if same as last
		uid = rfid.getUID()
		if uid is lastUID:
			continue
		print("UID: " + uid)
		#Tell redis who scanned, when, and where
		timestamp = calendar.timegm(time.gmtime())
		location = configurationDictionary["location"]
		result = redis.postScan(uid, timestamp, location)
		print("Result: " + result)
		lastUID = uid
		#Do we want to sleep/clear?

def launchLocationReader():
	lastUID = None
	while True:
		uid = None
		print("Waiting for scan")
		while not rfid.detectBand():
			pass
		print("Scanning")
		loc = rfid.readLocation()
		configurationDictionary["location"] = loc
		print("Location changed to " + loc)
		lastUID = uid

def launchRegistration():	
	lastUID = None
	while True:
		uid = None
		print("Enter 4 digit pin")
		pin = ""
		for i in range(4)
			pin.join(keypad.getKey())
		(name, size) = redis.postPin(pin)
		print("name: " + name)
		print("size: " + size)
		print("Waiting for scan")
		while not rfid.detectBand():
			pass
		print("Scanned")
		uid = rfid.getUID()
		resp = redis.postRegistration(pin, uid)
		print("Response: " + resp)
		lastUID = uid
		
#Prevent warnings from reusing IO ports
GPIO.setwarnings(False)

#TODO
#Change to logging.WARNING or ERROR for release
logging.basicConfig(filename='scanner.log', level=logging.DEBUG)
	
#TODO
#register mode switch interrupts
#GPIO.add_event_detect(pin, rising/falling edge, handlerFunction)

#TODO
#Load information from config file

#Launch into the scanner mode
launchScanner()
