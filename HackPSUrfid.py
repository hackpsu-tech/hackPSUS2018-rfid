"""
This module provides an abstraction on top of the MFRC522 library
That library can be found at https://github.com/mxgxw/MFRC522-python

Methods:
	detectBand()
		Get whether or not a band is on the scanner
	getUID()
		Get a wristband's UID as a string
	readLocation()
		Get the location written to the first sectors of the wristband
	writeLocation(location : str)
		Write the given location to the current wristband
"""
import sys
import io
import MFRC522

reader = MFRC522.MFRC522()
locationSector = 8
key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

def detectBand():
	"""
	bool detectBand ( void )
	
	Detect the first available rfid tag and get the reader status
	This is a nonblocking call
	
	Returns:
		bandPresent: True for a band present, or False for no band present
	
	"""
	(status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)
	if status == reader.MI_OK:
		return True
	return False

def getUID():
	"""
	str getUID ( void )
	
	Detect the first available rfid tag and get the UID
	This is nonblocking call
	
	Returns:
		value: A UID string formatted like "?,?,?,?"
	
	Raises:
		ValueError: This will be raised iff no wristband is available
	"""
	(status, uid) = reader.MFRC522_Anticoll()
	if not (status == reader.MI_OK):
		raise ValueError('No rfid tag detected')
	value = "{uid1},{uid2},{uid3},{uid4}".format(uid1=uid[0], uid2=uid[1], uid3=uid[2], uid4=uid[3])
	return value

def readLocation():
	"""
	str readLocation ( void )
	
	Detect the first available rfid tag and get the data from the locationSector
	
	Returns:
		location: A string from the data back from the tag
		
	Raises:
		ValueError: This will be raised if no wristband is available or the wrong amount of data is returned
	"""
	(status, uid) = reader.MFRC522_Anticoll()
	reader.MFRC522_SelectTag(uid)
	reader.MFRC522_auth(reader.PICC_AUTHENT1A, 8, key, uid)
	buffer = [0] * 4
	buffer[0] = reader.PICC_READ
	buffer[1] = locationSector
	pOut = reader.CalulateCRC(buffer)
	buffer[2] = pOut[0]
	buffer[3] = pOut[1]
	(status, backData, backLen) = reader.MFRC522_ToCard(reader.PCD_TRANSCEIVE, buffer)
	if not (status == reader.MI_OK):
		raise ValueError('No tag detected')
	if not (len(backData) == 16):
		raise ValueError('Incorrect number of bytes read')
	reader.MFRC522_StopCrypto1()
	return backData.decode()

def writeLocation(location):
	"""
	void writeLocation ( location:str )
	
	Detect the first available rfid tag and write the given location to the locationSector
	
	Args:
		location: The location to write to the wristband
		
	Raises:
		ValueError if there is no wristband available or the location is longer than 16 chars in length
	"""
	(status, uid) = reader.MFRC522_Anticoll()
	reader.MFRC522_SelectTag(uid)
	reader.MFRC522_auth(reader.PICC_AUTHENT1A, 8, key, uid)
	if len(location) > 16:
		raise ValueError('Location string is too long')
	buffer = location.encode()
	zeros = len(location) - 16
	for i in range(zeros):
		buffer.append(0)
	tmp_out = sys.stdout
	sys.stdout = io.BytesIO()
	reader.MFRC522_Write(locationSector, buffer)
	sys.stdout = tmp_out
	reader.MFRC522_StopCrypto1()

