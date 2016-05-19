import RPi.GPIO as GPIO
import time
import readchar

pwmY,dirY,pwmX,dirX,laser = 12,11,35,32,37

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwmY, GPIO.OUT)
GPIO.setup(dirY, GPIO.OUT)
GPIO.setup(dirX, GPIO.OUT)
GPIO.setup(pwmX, GPIO.OUT)
GPIO.setup(laser, GPIO.OUT)

GPIO.output(dirX, False)
GPIO.output(dirY, False)
GPIO.output(laser, False)
pY = GPIO.PWM(pwmY, 8000)
pX = GPIO.PWM(pwmX, 8000)
pX.start(0)
pY.start(0)

while(True):

	x = readchar.readchar()	
	if(x == 'a'):
		GPIO.output(dirX,False)
		pX.ChangeDutyCycle(100)
	elif(x == 'd'):
		GPIO.output(dirX,True)
		pX.ChangeDutyCycle(0)
	elif(x == 'w'):
		GPIO.output(dirY,True)
		pY.ChangeDutyCycle(0)
	elif(x == 's'): 
		GPIO.output(dirY,False)
		pY.ChangeDutyCycle(100)
	elif(x == 'l'):
		GPIO.output(laser,True)
	elif(x == 'k'):
		GPIO.output(laser,False)
	elif(x == 'x'): 
		GPIO.output(dirX,False)
		GPIO.output(dirY,False)
		pX.ChangeDutyCycle(0)
		pY.ChangeDutyCycle(0)
	elif(x == 'q'):
		GPIO.cleanup()
		exit()

