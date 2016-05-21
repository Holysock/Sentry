import RPi.GPIO as GPIO

class motor():
    pwmY,dirY,pwmX,dirX,laser = 12,11,35,32,37
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)   
    GPIO.setup(pwmY, GPIO.OUT)
    GPIO.setup(dirY, GPIO.OUT)
    GPIO.setup(dirX, GPIO.OUT)
    GPIO.setup(pwmX, GPIO.OUT)
    GPIO.setup(laser, GPIO.OUT)

    GPIO.output(laser, False)
    dY = GPIO.PWM(dirY, 8000)
    dX = GPIO.PWM(dirX, 8000)
    pY = GPIO.PWM(pwmY, 8000)
    pX = GPIO.PWM(pwmX, 8000)
    dX.start(0)
    dY.start(0)
    pX.start(0)
    pY.start(0)
    
    def __init__(self):
        GPIO.setwarnings(False)
        
    def setSpeedX(self,value):
        if value > 100: value = 100
        elif value < -100: value = -100
        elif abs(value) < 20: value = 0
        
        if value < 0: 
            value = ((abs(value)-20)/80.0)*100.0
            self.dX.ChangeDutyCycle(100)
            self.pX.ChangeDutyCycle(100-value)
            print "X-axis:{0}".format(value)
            
        elif value > 0:
            value = ((abs(value)-20)/80.0)*100.0
            self.dX.ChangeDutyCycle(0)
            self.pX.ChangeDutyCycle(value)
            print "X-axis:{0}".format(value)
            
        elif value == 0:
            self.dX.ChangeDutyCycle(0)
            self.pX.ChangeDutyCycle(0)
            
    def setSpeedY(self,value):
        if value > 100: value = 100
        elif value < -100: value = -100
        elif abs(value) < 20: value = 0
        
        if value < 0: 
            value = ((abs(value)-20)/80.0)*100.0
            self.dY.ChangeDutyCycle(100)
            self.pY.ChangeDutyCycle(100-value)
            print "Y-axis:{0}".format(value)
            
        elif value > 0:
            value = ((abs(value)-20)/80.0)*100.0
            self.dY.ChangeDutyCycle(0)
            self.pY.ChangeDutyCycle(value)
            print "Y-axis:{0}".format(value)
            
        elif value == 0:
            self.dY.ChangeDutyCycle(0)
            self.pY.ChangeDutyCycle(0)
            
            
             
