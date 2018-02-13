#! /bin/bash
#Get the location that the user wants entered into the first cell
read -p "Please enter your location: " location
if [ "$location" == "" ]
then
	echo "Invalid location"
	exit -1
fi

#Run ping.py using python (probably python2).  We need to update ws://localhost:5000/v1/pi to the actual server
python ping.py ws://localhost:5000/v1/pi 10 pings.csv $location

read -n1 -r -p "Press any key to continue..." key
