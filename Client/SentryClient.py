import socket
import pygame
import time
import sys

ID = 123456 # ID of Player connecting
TCP_IP = argv[1]
TCP_PORT = 1234
BUFFER_SIZE = 1024  
RETRY = 5 

#Joystick-stuff
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() > 0: 
    print "Client: Joystick has been initialized."
else:
    print "Cient: No Joystick found."
    exit(1)
    
stick = pygame.joystick.Joystick(0)
stick.init()
axisNum = stick.get_numaxes()

#TCP-stuff
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP,TCP_PORT))
except socket.error, e:
    print "Client: Error: {0}".format(e)
    exit(1)
    
try:
    s.sendall("ID{0}\n".format(ID))
    time.sleep(0.25)
except socket.error, e:
    print "Client: Sending Player ID: {0} failed: {1}".format(ID,e)
 
x = 0
while pygame.joystick.get_count()>0:
    pygame.event.get()
    stick_L = (stick.get_axis(0),stick.get_axis(1))
    stick_R = (stick.get_axis(3),stick.get_axis(4))
    pads = (stick.get_axis(2),stick.get_axis(5))
    
    try:
        s.sendall("LS {0} {1}".format(stick_L[0],stick_L[1]))
        time.sleep(0.005)
        s.sendall("RS {0} {1}".format(stick_R[0],stick_R[1]))
        time.sleep(0.005)
        s.sendall("PD {0} {1}".format(pads[0],pads[1]))
        time.sleep(0.005)
        x = 0
    except socket.error, e:
        print "Client: Sending stuff failed: {0}".format(e)
        x += 1
        if x == RETRY:
            print "Connection closed after {0} retries.".format(RETRY)
            s.close()
            exit(1) 
    
s.close()


