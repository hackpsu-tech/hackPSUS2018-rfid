"""
HackPSU Abstractions for communicating with the Redis cache via http using requests

@Julia please implement this bitch and maybe doc your method up here and put the redis url up here?

Requires requests (pip install requests)
"""
import requests

def postRegistration(uid, pin):
	"""
	(response:?) postRegistration (uid:str, pin:str)
	
	Associate a UID with a pin in the server to register a user
	
	Args:
		uid: A String for UID from the scan
		pin: A String for the user's pin
	
	Returns:
		response: A pass/fail signal (idc what the type is, just doc it)
	"""
	return ""
	
def postPin(pin):
	"""
	(name:str, size:str) postPin (pin:str)
	
	Query redis to get the user's name and shirt size from the server
	
	Args:
		pin: The 4 digit pin as a string
		
	Returns:
		name: The user's first and last name as a string
		size: The user's shirt size as a string
	"""
	return ("name","size")
	
def postScan(uid, timestamp, location):
	"""
	(result:?) postScan (uid:str, timestamp:float, location:str)
	
	Post a scan to redis and get a response
	response needs to say, g2g, halt, or error with redis
	
	Args:
		uid: A String for the UID from the scan
		timestamp: GMT Epoch time of the scan as a float (time.0)
		location: The location ID as a String from the scan
	
	Returns:
		result:	Something with at least 3 states for results, just doc their meanings
	"""
	return ""
