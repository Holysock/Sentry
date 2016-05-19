#!/usr/bin/env python

#
import socket
import Player

TCP_IP = 'kirapi'
TCP_PORT = 1234
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
ID = 0 # Player ID, the IR diode "shoots" this code 

def parse(date):
    if "RS" in data[:2]: #Parse Data into X and Y -> Controlls motor.
        values = data[3:]
        for i in xrange(len(values)):
            if values[i] == ' ':
                X = float(values[:i])
                Y = float(values[i+1:])
                player.moveSentry((X,Y))
                break
                    
    elif "LS" in data[:2]: #Parse Data into X and Y -> Currently this axis is not used.
        values = data[3:]
        for i in xrange(len(values)):
            if values[i] == ' ':
                X = float(values[:i])
                Y = float(values[i+1:])
                break
    
    elif "PD" in data[:2]: #Parse Data into Left and Right -> Toggels flashlight and lasergun.
        values = data[3:]
        for i in xrange(len(values)):
            if values[i] == ' ':
                L = float(values[:i])
                R = float(values[i+1:])
                player.setLight(L)
                player.shoot(R)
                print L,R
                break
          
    elif "HALT" in data[:4]:
        print "Server: Command: HALT."
        print "Server: Shutting down."
        connection.close()
        exit(0)
        
    else:
        return 1
                    
                    
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
    			data = connection.recv(BUFFER_SIZE)
    			if not data: 
				break
    			#print data
    			if "ID" in data and not ID:
    			    player = Player.player(data[2:])
    			elif parse(data):
    			    print "Server: unkown command: {0}".format(data)
 
		connection.close()
	except socket.error, e:
		print "Server: Connection lost."		
