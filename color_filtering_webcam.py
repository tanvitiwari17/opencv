# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:01:50 2020

@author: tanvi
"""

import cv2
import numpy as np

device = cv2.VideoCapture(0)

while True:
    ret,frame =device.read()
    
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #for skin color :
    lower_range = np.array([0,10,60]) 
    upper_range = np.array([20,150,255])
    
    """
        #for blue color :
    lower_range = np.array([110,50,50]) 
    upper_range = np.array([130,255,255])

    """
    mask = cv2.inRange(hsv,lower_range,upper_range)
    cv2.imshow("show1",mask)
    cv2.imshow("show2", frame)
    
    if cv2.waitKey(1)==13:
        break
device.release()
cv2.destroyAllWindows()
    