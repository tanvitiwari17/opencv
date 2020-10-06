# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:45:28 2020

@author: tanvi
"""

import cv2
import numpy as np

img = cv2.imread("Lenna.png")

cv2.imshow("Original",img)
cv2.waitKey(0)

# creating a matrix to perform arithmetic

M = np.ones(img.shape, dtype ='uint8') * 150
# or  M = np.ones(img.shape, dtype ='uint8') + 150

# add

added = cv2.add(img,M)
cv2.imshow('Addition',added)
cv2.waitKey(0)

# subtact

subtracted = cv2.subtract(img,M)
cv2.imshow('Subtraction',subtracted)
cv2.waitKey(0)

# multiplication

multiple=cv2.multiply(img,M)
cv2.imshow("Multiplication",multiple)
cv2.waitKey(0)
cv2.destroyAllWindows()