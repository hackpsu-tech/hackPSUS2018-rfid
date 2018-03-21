#!/usr/bin/python

#import hackpsu.RFID

#raw_input for py2 or input for py3
while True:
	location = input("Enter a location ID")
	print("Location registered as: " + location)
	print("Please scan an RFID tag now")
	
	#uid = RFID.getUID
	#RFID.target(uid)
	#RFID.authenticated(key)
	#RFID.write(location.encode)
	#readBack = RFID.read()
	#RFID.clearTarget
	
	#print("Write success; wrote: " + readBack.decode)