#!/usr/bin/env python3

import cv2
import numpy as np
import rospy
from std_msgs.msg import UInt16



pub = rospy.Publisher('servo', UInt16, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) 

cap = cv2.VideoCapture(0)
x_medium = 5

while True:
	_, frame = cap.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	
	# green
	low_green = np.array([40, 70, 70])
	high_green = np.array([70, 255, 255])
	green_mask = cv2.inRange(hsv_frame, low_green, high_green)
	contours,hierachy=cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
	contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
	
	for cnt in contours:
		(x, y, w, h) = cv2.boundingRect(cnt)
		
		x_medium = int((x + x + w) / 2)
		
		value = x_medium
		rospy.loginfo(value)
		pub.publish(value)
		rate.sleep()
		
		break
	
	cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
	
	cv2.imshow("Frame", frame)
	
	
	key = cv2.waitKey(1)
	
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()
