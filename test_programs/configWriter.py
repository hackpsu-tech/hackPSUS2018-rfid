#!/usr/bin/python
"""
This application reads key value pairs from the command line input and writes to a dictionary, which is then written to a config file
The preferred file extension is .cfg
"""
import signal
import sys
import HackPSUconfig as config

#Initialize a dictionary and define the save and configFile variables
#save is initialized to False to prevent the signal handler form saving if the program quits before a file is given
dict = {}
configFile = None
save = False

def signal_handler(signal, frame):
	"""
	void signal_handler (signal, frame)
	
	This function handles the system signal SIGINT
	The purpose of this function is to save before quitting
	
	Args:
		signal: The signal from the OS
		frame: The current stack frame
		
	"""
	print('\nSIGINT captured; save and quit initiated.')

	#If we have a 
	if configFile != None:
		config.setProperties(configFile, dict)
	
	sys.exit(0)

#Register our signal handler
signal.signal(signal.SIGINT, signal_handler)
#Read the input file
configFile = input('Enter a configuration file name: ')
print('Press Ctrl+C to save and quit\n')

#Loop until program is force killed
while(True):
	#Read in a key, value pair and load it into the dictionary
	key = input('Please enter a key: ')
	value = input('Please enter a value: ')
	dict[key] = value
	print('Dictionary entry for ' + key+ ':' + dict[key] + ' created successfully')
	print('')
	