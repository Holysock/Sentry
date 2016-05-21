#Player class. The Player does all the things regarding motorcontroll
import MotorControll

class player:
    ID = 0
    X = 0 
    Y = 0
    light = 0
    motor = 0
    def __init__(self,ID):
        self.ID = int(ID)
        print "Player: Player ID:" ,self.ID
        self.motor = MotorControll.motor()
        self.motor.__init__()
    def moveSentry(self,data):
        print data 
        self.X = data[0]*100
        self.Y = data[1]*100
        self.motor.setSpeedX(self.X)
        self.motor.setSpeedY(self.Y)
    def setLight(self,data):
        self.light = data 
    def shoot(self,data):
        pass #later: pass ID to IR transmitter
         
