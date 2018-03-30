"""
This module pretends to be HackPSUlcd but uses print to console instead

"""

DATA_ROW = 2
DEBUG_ROW = 1

def clearRow(row):
	print("\n")

def printDebug(location, wifi):
	clearRow(DEBUG_ROW)
	print("Loc: " + location + ", " + wifi + "%")

def printScan(goodScan):
	clearRow(DATA_ROW)
	print("Allow in: " + goodScan)
	
def printName(name):
	clearRow(DEBUG_ROW)
	clearRow(DATA_ROW)
	print(name)
	print("#: Retry, *:Go")
	
def printSize(size):
	clearRow(DATA_ROW)
	print("Size: " + size)

def printLocation(location):
	clearRow(DATA_ROW)
	print("Location: " + location)
	
def printRegistered(registered):
	clearRow(DATA_ROW)
	print("Registered: " + registered)
	
def printMsg(msg):
	clearRow(DATA_ROW)
	print(msg)
