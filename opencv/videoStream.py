from imutils.object_detection import non_max_suppression
from imutils.video import WebcamVideoStream
import imutils
import cv2
import numpy

vs = WebcamVideoStream(src=0).start()
SIZE_W = 300

while(True):
	frame = vs.read()
	cv2.imshow('Video',imutils.resize(frame, width=min(SIZE_W, frame.shape[1])))
	if cv2.waitKey(10) & 0xFF == ord('q'):
                break

