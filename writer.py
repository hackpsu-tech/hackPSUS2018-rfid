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

#TODO
#import hackpsu.RFID

#TODO
#Load keys from config file

#raw_input for py2 or input for py3
while True:
	location = input("Enter a location ID")
	print("Location registered as: " + location)
	print("Please scan an RFID tag now")
	
	#TODO
	#uid = RFID.getUID
	#RFID.target(uid)
	#RFID.authenticated(key)
	#RFID.write(location.encode)
	#readBack = RFID.read()
	#RFID.clearTarget
	
	#print("Write success; wrote: " + readBack.decode)
	print("Please remove wristband")