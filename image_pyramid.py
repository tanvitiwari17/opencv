# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:29:26 2020

@author: tanvi
"""

#image resize using image Pyramid

import cv2
import numpy as np

img = cv2.imread("Lenna.png")

smaller = cv2.pyrDown(img)
larger = cv2.pyrUp(img)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.imshow("Smaller", smaller)
cv2.waitKey(0)
cv2.imshow("Larger", larger)
cv2.waitKey(0)
cv2.destroyAllWindows()