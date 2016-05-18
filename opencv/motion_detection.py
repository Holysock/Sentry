import cv2
import numpy as np
import os
import plotlib

plotter = plotlib.plot()
plotter.setBackground(0,0,0)
dim = plotter.getDim()

video_capture = cv2.VideoCapture(0)

t_minus = cv2.cvtColor(video_capture.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(video_capture.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(video_capture.read()[1], cv2.COLOR_RGB2GRAY)

def diffImg(t0, t1, t2):
	d1 = cv2.absdiff(t2, t1)
	d2 = cv2.absdiff(t1, t0)
	return cv2.bitwise_and(d1, d2)

def show(img):
	for x in xrange(dim[0]):
		for y in xrange(dim[1]):
			plotter.setColor(img.item(y,x,3),img.item(y,x,2),img.item(y,x,1))

while True:
	img = ("Motion",diffImg(t_minus, t, t_plus))
	show(img)

	t_minus = t
	t = t_plus
	t_plus = cv2.cvtColor(video_capture.read()[1], cv2.COLOR_RGB2GRAY)

	if cv2.waitKey(10) & 0xFF == ord('q'):
        	break	

video_capture.release()
#cv2.destroyAllWindows()
	
	
