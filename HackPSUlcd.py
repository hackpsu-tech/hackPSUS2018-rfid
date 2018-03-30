"""
This module provides abstractions on top of the LCD library
Requires: https://gist.github.com/DenisFromHR/cc863375a6e19dce359d

"""
import I2C_LCD_Driver

MY_LCD = I2C_LCD_Driver.lcd()
DEBUG_ROW = 1
DATA_ROW = 2

def clearRow(row):
	nullStr = ""
	for i in range(16):
		nullStr.join(" ")
	MY_LCD.lcd_display_string(nullStr, row)

def printDebug(location, wifi):
	clearRow(DEBUG_ROW)
	MY_LCD.lcd_display_string("Loc: " + location + ", " + wifi + "%", DEBUG_ROW)

def printName(name):
	clearRow(DEBUG_ROW)
	clearRow(DATA_ROW)
	MY_LCD.lcd_display_string(name, DEBUG_ROW)
	MY_LCD.lcd_display_string("#: Retry, *:Go")

def printSize(size):
	clearRow(DATA_ROW)
	MY_LCD.lcd_display_string("Size: " + size, DATA_ROW)

def printScan(goodScan):
	clearRow(DATA_ROW)
	MY_LCD.lcd_display_string("Allow in: " + goodScan, DATA_ROW)

def printLocation(location):
	clearRow(DATA_ROW)
	MY_LCD.lcd_display_string("Location: " + location, DATA_ROW)
	
def printRegistered(registered):
	clearRow(DATA_ROW)
	MY_LCD.lcd_display_string("Registered: " + registered, DATA_ROW)
	
def printMsg(msg):
	clearRow(DATA_ROW)
	MY_LCD.lcd_display_string(msg, DATA_ROW)
