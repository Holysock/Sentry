#!/usr/bin/env python

import socket


TCP_IP = '172.0.0.1'
TCP_PORT = 1234
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while 42:
	try:
		connection, address = s.accept()
		print 'Connection address:', address
	except socket.timeout:
		print "Timeout."
		break
	try:
		while 42:
    			data = connection.recv(BUFFER_SIZE)
    			if not data: 
				break
    			print "received data:", data
			connection.send(data)  # echo
		connection.close()
	except socket.error, e:
		print "Connection lost."		
