import pygame
import time

pygame.init()
pygame.joystick.init()

#print [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())], pygame.joystick.get_count()

if pygame.joystick.get_count() > 0: 
    print "Joystick has been initialized."
else:
    print "No Joystick found."
    exit(1)
	
stick = pygame.joystick.Joystick(0)
stick.init()
axisNum = stick.get_numaxes()

while pygame.joystick.get_count()>0:
    pygame.event.get()
    stick_L = (stick.get_axis(0),stick.get_axis(1))
    stick_R = (stick.get_axis(3),stick.get_axis(4))
    pads = (stick.get_axis(2),stick.get_axis(5))
    
    #time.sleep()


