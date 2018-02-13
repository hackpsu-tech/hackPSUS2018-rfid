#! /bin/bash
read -p "Please enter your location: " location
if [ "$location" == "" ]
then
	echo "Invalid location"
	exit -1
fi

python ping.py ws://localhost:5000/v1/pi 10 pings.csv $location
read -n1 -r -p "Press any key to continue..." key
