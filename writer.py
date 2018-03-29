#!/usr/bin/python
"""
This application writes strings read in from the terminal to a wristband
This application writes string data to the RFID tag and does not verify the number of sectors on the wristbands

The general use is:
	SSH into PI
	Remove all RFID tags from scanner
	Start Program:
	Enter location string
	Place RFID tag on scanner
	Verify that location was written correctly
	Remove tag from scanner 
	goto Start Program
"""

import HackPSUrfid as rfid
import time

#raw_input for py2 or input for py3
while True:
	print("Please place wristband on scanner")
	location = raw_input("Enter a location ID: ")
	print("Location registered as: " + location)
	print("Please scan an RFID tag now")
	
	if not rfid.detectBand():
		continue
		
	uid = rfid.getUID()
	print("Writing to UID: " + uid)
	
	oldLoc = rfid.readLocation()
	print("Old location string: " + oldLoc)
	
	rfid.writeLocation(location)
	
	newLoc = rfid.readLocation()
	print("New location string: " + newLoc)
	
	print("Please remove wristband")
	time.sleep(1)
