#!/usr/bin/env python

#
import socket
#import Player
import sys

TCP_IP = sys.argv[1]
TCP_PORT = 1234
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
ID = 0 # Player ID, the IR diode "shoots" this code 

def getIndexOfSub(data,sub):
    if sub in data:
        index = 0
        c = sub[0] # c is very cool
        for ch in data:
                if  ch == c and data[index:index+len(sub)] == sub: 
                    break
                else:
                    index += 1
        while sub in data[index+len(sub):] and index+len(sub) < len(data):
            index += 1
            for ch in data[index+len(sub)]:
                if  ch == c and data[index:index+len(sub)] == sub: 
                    break
                else:
                    index += 1
        return index
    else:
        return -1

def parse(data):
    if "RX" in data:
        try:
            start = getIndexOfSub(data,"RX")
            if start == -1 or not ('Y' in data[start:] and '#' in data[start:]): 
                raise ValueError("Message corrupted")
            stop = start+3
            for ch in data[start+2:]:
                if stop >= len(data): raise ValueError("stop >= len(data), 1")
                if ch == 'Y': break
                else: stop += 1
            if stop > BUFFER_SIZE: raise ValueError("stop > BUFFER_SIZE:")
            X = float(data[start+2:stop-1])
            print "X {0}".format(X)
            start = stop     
            stop = start+1
            for ch in data[start+1:]:
                if stop >= len(data): raise ValueError("stop >= len(data), 2")
                if ch == '#': break
                else: stop += 1 
            if stop > BUFFER_SIZE: raise ValueError("stop > BUFFER_SIZE:")
            Y = float(data[start:stop])
            print "Y {0}".format(Y)   
        except ValueError as error:
            print "Error in parse RX: {0}".format(error) 
        
        #if "ID" in data and not ID:
        #    player = Player.player(data[2:])
                    
print "Server: Server started."
while 42:
	try:
		connection, address = s.accept()
		print 'Server: Connection address:', address
	except socket.timeout:
		print "Server: Timeout."
		break
	try:
		while 42:
    			data_stream = connection.recv(BUFFER_SIZE)
    			print data_stream
    			if data_stream: 
				    try: 
				        parse(data_stream)
				    except ValueError as error:
				        print "Server: Error: {0}".format(error) 
 
		connection.close()
	except socket.error, e:
		print "Server: Connection lost."		
