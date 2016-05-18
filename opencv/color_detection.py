from imutils.object_detection import non_max_suppression
from imutils.video import WebcamVideoStream
import imutils
import cv2
import numpy as np
import sys
import colorsys
import time
import RPi.GPIO as GPIO


SIZE_W = 200
fpsCountMAX = 10
fpsCount = 0
t = time.clock()

lower1 = np.array([0, 120, 100],np.uint8)
upper1 = np.array([5, 255, 255],np.uint8)

lower2 = np.array([170, 120, 100],np.uint8)
upper2 = np.array([180, 255, 255],np.uint8)

#lower3 = np.array([105, 100, 70],np.uint8)
#upper3 = np.array([135, 255, 255],np.uint8)

vs = WebcamVideoStream(src=0).start()
#vs = cv2.VideoCapture(0)
frame = vs.read()
frame = imutils.resize(frame, width=min(SIZE_W, frame.shape[1]))
center_of_frame = (int(frame.shape[1]/float(2)),int(frame.shape[0]/float(2)))
target_rect = 4

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
pwmX = GPIO.PWM(35,1000)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
pwmY = GPIO.PWM(12,1000)

GPIO.output(36, False)
GPIO.output(11, False)
GPIO.output(37, False)
pwmX.start(0)
pwmY.start(0)

Kp = 0.6
Ki = 0.005
Kd = 0.4

u_pX = 0
u_pY = 0 
u_iX = 0
u_iY = 0
u_dX = 0
u_dY = 0
u_gesX = 0
u_gesY = 0
l_etX = 0
l_etY = 0

def moveX(dir,et):
	global u_pX
	global u_iX
	global u_gesX
	global l_etX
	if dir == 2:
                GPIO.output(36,False)
                pwmX.ChangeDutyCycle(0)
		#u_pX = 0
		u_iX = 0
		#u_dX = 0
		return

	flag = 1-2*dir
	u_pX = et*Kp
	u_iX += et*Ki*flag
	if u_iX > 20:
		u_iX = 20
	elif u_iX < -20:
		u_iX = -20
	u_dX = abs(l_etX-et*flag)*Kd
	l_etX = et*flag
	u_gesX = u_pX + u_dX + abs(u_iX)
	if u_gesX > 100:
		u_gesX = 100
	elif u_gesX < 0:
		u_gesX = 0
	if (abs(u_iX) > (u_dX + u_pX)):
		u_gesX = 15 
	#print u_gesX,u_iX,u_pX
	if dir == 0:
		GPIO.output(36,True)		
		pwmX.ChangeDutyCycle(100-u_gesX)
	elif dir == 1:
		GPIO.output(36,False)
		pwmX.ChangeDutyCycle(u_gesX)
	else: 
		GPIO.output(36,False)
		pwmX.ChangeDutyCycle(0)
	
def moveY(dir,et):
	global u_pY
        global u_iY
        global u_gesY
        global l_etY
        if dir == 2:
                GPIO.output(11,False)
                pwmY.ChangeDutyCycle(0)
                #u_pY = 0
                u_iY = 0
                #u_dY = 0
                return

        flag = 1-2*dir
        u_pY = et*Kp
        u_iY += et*Ki*flag
        if u_iY > 20:
                u_iY = 20
        elif u_iY < -20:
                u_iY = -20
        u_dY = abs(l_etY-et*flag)*Kd
	l_etY = et*flag
        u_gesY = u_pY + u_dY + abs(u_iY)
        if u_gesY > 100:
                u_gesY = 100
        elif u_gesY < 0:
                u_gesY = 0
	if (abs(u_iY) > (u_dY + u_pY)):
                u_gesY = 15

        #print u_gesY,u_iY,u_pY
        if dir == 0:
                GPIO.output(11,True)
                pwmY.ChangeDutyCycle(100-u_gesY)
        elif dir == 1:
                GPIO.output(11,False)
                pwmY.ChangeDutyCycle(u_gesY) 
idle = 1 	

while True:
	idle = 1
	frame = vs.read() 
	frame = imutils.resize(frame, width=min(SIZE_W, frame.shape[1]))
	frame_HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	mask1 = cv2.inRange(frame_HSV, lower1, upper1)
	mask2 = cv2.inRange(frame_HSV, lower2, upper2)
	#mask = cv2.inRange(frame_HSV, lower3, upper3)
	#mask12 = cv2.bitwise_or(mask1,mask2)
	mask = cv2.bitwise_or(mask1,mask2)
	
	kernel = np.ones((3,3),np.uint8)
	#opening = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	#opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)
	dilate = cv2.dilate(mask,kernel,iterations = 10)

	dist = cv2.distanceTransform(dilate,cv2.cv.CV_DIST_L2,cv2.cv.CV_DIST_MASK_PRECISE)
	cv2.normalize(dist,dist,alpha = 0.0, beta = 1.0, norm_type=cv2.NORM_MINMAX)
	
	minVal,maxVal,minLoc,center = cv2.minMaxLoc(dist) # 'center' is center of target, not center of frame
	if not minVal == maxVal:
		cv2.line(frame,(center[0]-20,center[1]),(center[0]+20,center[1]),(0,255,0),2) #cross on target
		cv2.line(frame,(center[0],center[1]-20),(center[0],center[1]+20),(0,255,0),2)
		cv2.line(frame,(center[0],center[1]),(int(frame.shape[1]/2),int(frame.shape[0]/2)),(255,0,0),2) #target line
	
		cv2.line(dist,(center[0]-20,center[1]),(center[0]+20,center[1]),255,2) #cross on target
		cv2.line(dist,(center[0],center[1]-20),(center[0],center[1]+20),255,2)
		cv2.line(dist,(center[0],center[1]),(int(frame.shape[1]/2),int(frame.shape[0]/2)),255,2) #target line
		
		lockedX = 0
		lockedY = 0

		if center[0] < center_of_frame[0]-target_rect:
			moveX(0,100-100*(center[0]/float(center_of_frame[0])))
			#print "< {0}" .format(100-100*(center[0]/float(center_of_frame[0])))
		elif center[0] > center_of_frame[0]+target_rect:
			moveX(1,100*((center[0]-center_of_frame[0])/float(center_of_frame[0])))
			#print "> {0}" .format(100*((center[0]-center_of_frame[0])/float(center_of_frame[0])))
		else:
			moveX(2,0)
			lockedX = 1

		if center[1] < center_of_frame[1]-target_rect:
			moveY(0,100-100*(center[1]/float(center_of_frame[1])))
			#print "^"
		elif center[1] > center_of_frame[1]+target_rect:
			moveY(1,100*((center[1]-center_of_frame[1])/float(center_of_frame[1])))
			#print "v"
		else:
			moveY(2,0)
			lockedY = 1

		if lockedX and lockedY:
			GPIO.output(37, True)
			print "PEW! PEW!"
		else:
			GPIO.output(37, False) 
	else:
		GPIO.output(37, False)
		GPIO.output(36,False)
		GPIO.output(12,False)
		pwmX.ChangeDutyCycle(0)
		pwmY.ChangeDutyCycle(0)
		if idle >= 1 and idle < 2:
			idle += 1
#	                GPIO.output(36,False)
#	                pwmX.ChangeDutyCycle(50)
		elif idle >= 15:
			idle = 0
		elif idle <= 0 and idle > -2:
			idle -= 1
#			GPIO.output(36,True)
#                       pwmX.ChangeDutyCycle(50)
		elif idle <= -15:
			idle = 1
		moveY(2,0)

	cv2.rectangle(frame,(center_of_frame[0]-target_rect,center_of_frame[1]-target_rect),(center_of_frame[0]+target_rect,center_of_frame[1]+target_rect),(0,0,255),2)
	cv2.imshow('orginal', frame)
	cv2.imshow('dist', dist)
	#cv2.moveWindow('orginal', 0, 0)
	#cv2.moveWindow('dist',SIZE_W, 0)
	
	if fpsCount <= fpsCountMAX:
		fpsCount += 1
	else:
		dt = time.clock()-t
		print("FPS: {0}" .format(fpsCount/float(dt)))
		fpsCount = 0
		t = time.clock()

	if cv2.waitKey(10) & 0xFF == ord('q'):
        	GPIO.cleanup()
		break
	
video_capture.release()
cv2.destroyAllWindows()



#def getPOIs(frame):
#	POI = []
#	POI[:] = []
#	for row in xrange(frame.shape[0]):
#		for col in xrange(frame.shape[1]):
#			if frame.item(row,col) >= 200:
#				POI.append((row,col))
#	return POI

#def getCenter(frame):
#	cx = 0
#	cy = 0
#	d = float(len(frame))
#	for f in frame:
#		cx += f[0]
#		cy += f[1]
#	return (int(cx/d),int(cy/d))
