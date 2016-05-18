#Player class. The Player does all the things regarding motorcontroll
#import RPi.GPIO as GPIO

pwmX, dirX, pwmY, dirY, Laser = 35,36,12,11,37

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pwmY, GPIO.OUT)
#GPIO.setup(dirY, GPIO.OUT)
#GPIO.setup(dirX, GPIO.OUT)
#GPIO.setup(pwmX, GPIO.OUT)
#GPIO.setup(Laser, GPIO.OUT)

class player:
    ID = 0
    X = 0 
    Y = 0
    light = 0
    def __init__(self,ID):
        self.ID = int(ID)
        print "Player: Player ID:" ,self.ID
    def moveSentry(self,data): 
        self.X = data[0]
        self.Y = data[1]
    def setLight(self,data):
        self.light = data 
    def shoot(self,data):
        pass #later: pass ID to IR transmitter
         
