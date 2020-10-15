# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:54:12 2020

@author: tanvi
"""
# convex hull : 
#technique to find out the pixel of outer edges of any abject and connects them 

import cv2
import numpy as np

hand = cv2.imread('cap.jpg',0)

ret, the = cv2.threshold(hand,70,255,cv2.THRESH_BINARY)

# to find connected pixels

contours,_= cv2.findContours(the.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) 
# returns contour and hierarchy, we only require contour here.

hull = [cv2.convexHull(c) for c in contours]

final = cv2.drawContours(hand,hull,-1,(255,0,0))

cv2.imshow("Original",hand)
cv2.imshow('Thresh', the)
cv2.imshow("Convex Hull",final) 
cv2.waitKey(0)
cv2.destroyAllWindows()
