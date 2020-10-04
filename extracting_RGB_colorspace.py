# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:12:32 2020

@author: tanvi
"""

import cv2
import numpy as np

img =cv2.imread("E:\pyWork\pyProjects\opencv\Lenna.png")

cv2.imshow("Original",img)
cv2.waitKey(0)

B,G,R = cv2.split(img)

zeros = np.zeros(img.shape[:2],dtype="uint8") # zero matrix of shape height and width 
cv2.imshow("Red",cv2.merge([zeros,zeros,R])) # merging image, B and G are 0 here
cv2.waitKey(0)

#similarly
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)

cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()