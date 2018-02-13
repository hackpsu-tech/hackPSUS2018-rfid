import sys
from websocket import create_connection
import time

if len(sys.argv) != 5:
    print('Usage: ping.py <apiLocation> <npings> <csvfile> <location>')
    sys.exit(-1)

print(sys.argv[1])
clientSocket = create_connection(sys.argv[1])
file = open(sys.argv[3], 'a+')
file.write(sys.argv[4])

for i in range(0, int(sys.argv[2])):
    clientSocket.send(str(time.time()))
    receive = clientSocket.recv()
    rtt = time.time() - float(receive)
    print('RTT ' + str(i) + ':\t' + str(rtt) + ' seconds')
    file.write(',' + str(rtt))

file.write('\n')
file.close()
clientSocket.close()
