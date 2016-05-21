from imutils.object_detection import non_max_suppression
from imutils.video import WebcamVideoStream
import imutils
import cv2
import numpy as np

SIZE_W = 200

vs = WebcamVideoStream(src=0).start()
frame = vs.read()
frame = imutils.resize(frame, width=min(SIZE_W, frame.shape[1]))
center_of_frame = (int(frame.shape[1]/float(2)),int(frame.shape[0]/float(2)))

while(42):
    frame = vs.read()
    frame = imutils.resize(frame, width=min(SIZE_W, frame.shape[1]))
    cv2.line(frame,(center_of_frame[0],center_of_frame[1]-20),(center_of_frame[0],center_of_frame[1]+20),(0,255,0),2)
    cv2.line(frame,(center_of_frame[0]-20,center_of_frame[1]),(center_of_frame[0]+20,center_of_frame[1]),(0,255,0),2)
    
    cv2.imshow('SentryV1', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
		break
