# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:48:48 2020

@author: tanvi
"""
# to directly rotate by 90 degrees
import cv2
import numpy as np

img = cv2.imread("Lenna.png")

rotated_img =cv2.transpose(img)

cv2.imshow("Original",img)
cv2.imshow("Rotated", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()