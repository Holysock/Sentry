#from imutils.video import WebcamVideoStream
#import cv2
import RPi.GPIO as GPIO
import time
import readchar

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

GPIO.output(36, False)
GPIO.output(11, False)
GPIO.output(37, False)
q = GPIO.PWM(12, 8000)
p = GPIO.PWM(35, 8000)
p.start(0)
q.start(0)

#vs = WebcamVideoStream(src=0).start()
#frame = vs.read()

while(True):
#	frame = vs.read()
#	cv2.imshow('Video',frame)
	x = readchar.readchar()	
	if(x == 'a'):
		GPIO.output(36,False)
		p.ChangeDutyCycle(100)
	elif(x == 'd'):
		GPIO.output(36,True)
		p.ChangeDutyCycle(0)
	elif(x == 'w'):
		GPIO.output(11,True)
		q.ChangeDutyCycle(0)
	elif(x == 's'): 
		GPIO.output(11,False)
		q.ChangeDutyCycle(100)
	elif(x == 'l'):
		GPIO.output(37,True)
	elif(x == 'k'):
		GPIO.output(37,False)
	elif(x == 'x'): 
		GPIO.output(36,False)
		GPIO.output(11,False)
		p.ChangeDutyCycle(0)
		q.ChangeDutyCycle(0)
	elif(x == 'q'):
		GPIO.cleanup()
		exit()
#	if cv2.waitKey(10) & 0xFF == ord('q'):
#                GPIO.cleanup()
#                break

