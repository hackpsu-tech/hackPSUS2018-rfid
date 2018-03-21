#!/usr/bin/python
"""
This application is intended to run on RaspberryPi startup and requires no console input
The application has four states, an initialization state, a location reader state, a wristband scanner state, and a wristband registration state
In this application, interrupts are triggered by button presses according to the attached schematic

Initialization State:
	All global variables are initialized
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
import threaing
import logging

try:
	import RPi.GPIO as GPIO
except ImportError:
	logging.ERROR('RaspberryPi GPIO is unavailable; please check OS installation')
	exit(-1)

#TODO: import all HackPSU abstraction modules
#import hackpsuLCD as lcd
#import hackpsuRFID as rfid
#import hackpsuKEYPAD as keypad
#import hackpsuREDIS as redis
	
#Prevent warnings from reusing IO ports
GPIO.setwarnings(False)

#Change to logging.WARNING or ERROR for release
logging.basicConfig(filename='scanner.log', level=logging.DEBUG)
	
#register mode switch interrupts
#GPIO.add_event_detect(pin, rising/falling edge, handlerFunctoin	

def launchScanner():
	
def launchWriter():

def launchRegistration():	