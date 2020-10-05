# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:55:14 2020

@author: tanvi
"""
# scaling resizing and interpolation

import cv2
import numpy as np

img = cv2.imread("Lenna.png")

cv2.imshow("Original", img)
cv2.waitKey(0)

# making size of the image 3/4 of it's original size
# Linear -> to reduce size
# Cubic -> to increase size

img_scaled = cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow("Scaling - Linear Interpolation",img_scaled)
cv2.waitKey()

# doubling the size of the image
img_scaled1=cv2.resize(img,None,fx=2,fy=2,interpolation = cv2.INTER_CUBIC)
cv2.imshow("Scaling - Cubic Interpolation", img_scaled1)
cv2.waitKey()

# skew the re-sizing by setting exxact dimensions
img_scales2= cv2.resize(img,(900,400),interpolation = cv2.INTER_AREA)
cv2.imshow("Scaling - Skewed Size",img_scales2)
cv2.waitKey()
cv2.destroyAllWindows()
