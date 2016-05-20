import RPi.GPIO as GPIO

class motor:
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
    
    def __init__(self):
        GPIO.setwarnings(False)
        
    def setSpeedX(self,value):
        if value > 100: value = 100
        elif value < -100: value = -100
        if value > 0:
            #self.GPIO.output(self.dirX, False)
            self.pX.ChangeDutyCycle(value)
        elif value < 0:
            self.GPIO.output(self.dirX, True)
            self.pX.ChangeDutyCycle(value+100)
            
            
            
             
