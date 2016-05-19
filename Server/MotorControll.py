import RPi.GPIO as GPIO

class motor:
    pwmY,dirY,pwmX,dirX,laser = 12,11,35,32,37
    
    def __init__(self):
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BOARD)   
        GPIO.setup(self.pwmY, GPIO.OUT)
        GPIO.setup(self.dirY, GPIO.OUT)
        GPIO.setup(self.dirX, GPIO.OUT)
        GPIO.setup(self.pwmX, GPIO.OUT)
        GPIO.setup(self.laser, GPIO.OUT)

        GPIO.output(self.dirX, False)
        GPIO.output(self.dirY, False)
        GPIO.output(self.laser, False)
        pY = GPIO.PWM(self.pwmY, 8000)
        pX = GPIO.PWM(self.pwmX, 8000)
        pX.start(0)
        pY.start(0)
        
    def setSpeedX(self,value):
        if value > 100: value = 100
        elif value < -100: value = -100
        if value > 0:
            GPIO.output(self.dirX, False)
            self.pX.ChangeDutyCycle(value)
        elif value < 0:
            GPIO.output(self.dirX, True)
            self.pX.ChangeDutyCycle(value+100)
            
            
            
             
