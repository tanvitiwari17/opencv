# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:45:51 2020

@author: tanvi
"""

import cv2
def sketch(image):
    # grascale
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # blurring
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    # edge detection
    canny_edge = cv2.Canny(img_gray_blur,10,70)
    
    ret,mask = cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY)
    
    return mask
    
cap=cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow("Our Live Sketch",sketch(frame))
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()