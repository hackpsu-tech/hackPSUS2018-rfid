import sys
from websocket import create_connection
import time

#Warn the user of how to use this if they give the wrong argc
if len(sys.argv) != 5:
    print('Usage: ping.py <apiLocation> <npings> <csvfile> <location>')
    sys.exit(-1)

#Print the location that we're connecting to, then connect
print(sys.argv[1])
clientSocket = create_connection(sys.argv[1])

#Open the CSV to append and add the first cell, the location
file = open(sys.argv[3], 'a+')
file.write(sys.argv[4])

#For each ping requested, add a cell with the RTT in seconds & print it out
for i in range(0, int(sys.argv[2])):
    clientSocket.send(str(time.time()))
    receive = clientSocket.recv()
    rtt = time.time() - float(receive)
    print('RTT ' + str(i) + ':\t' + str(rtt) + ' seconds')
    file.write(',' + str(rtt))

#Finish the row and close our resources
file.write('\n')
file.close()
clientSocket.close()
