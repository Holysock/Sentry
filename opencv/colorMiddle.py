import cv2
import numpy as np

DIVIDES = float(2) 
cam = cv2.VideoCapture(0)

ret, frame = cam.read()
size = (frame.shape[0],frame.shape[1]) #y,x / row, col
print size

def divide(frame):
	parts = []
	parts[:]=[]
	for ky in xrange(int(DIVIDES)):
		for kx in xrange(int(DIVIDES)):
			parts.append(frame[int((size[0]/DIVIDES)*ky):int((size[0]/DIVIDES)*(ky+1)),int((size[0]/DIVIDES)*kx):int((size[0]/DIVIDES)*(kx+1))])
	return parts

while True:
	ret,frame = cam.read()
	parts = divide(frame)
	
	if cv2.waitKey(10) & 0xFF == ord('q'):
        	break	 

	# show the images
	cv2.imshow('Video', frame)
	for i in xrange(len(parts)):
		cv2.imshow("%s" %(i), parts[i])
		print "{0}, {1}" .format(i,parts[i].mean())

