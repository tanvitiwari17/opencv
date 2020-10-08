# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:11:12 2020

@author: tanvi
"""
import cv2

cap = cv2.VideoCapture(0) # to access webcam

# to create an infinite loop
while True:
    ret,frame = cap.read()
    cv2.imshow("Our Live Sketch",frame)
    if cv2.waitKey(1)==13: # 13 is ascii code for enter
        break  
cap.release()
cv2.destroyAllWindows()
    
    
