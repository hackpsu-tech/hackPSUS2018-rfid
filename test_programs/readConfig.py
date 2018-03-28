#!/usr/bin/python
"""
This application simply reads a config file created by the HackPSUconfig module and prints the output to the console
"""

import HackPSUconfig as config

configFile = input('Please enter the name of a configuration file: ')
dict = config.getProperties(configFile)

print('Dictionary:')
for key in dict:
	print(key + ':' + dict[key])

print('Dictionary complete')	