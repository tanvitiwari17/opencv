# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:29:49 2020

@author: tanvi
"""

import cv2

img = cv2.imread('E:\pyWork\pyProjects\opencv\image1.jpg')


cv2.imshow('Output Image', img)
#imshow can only be used with waitKey()

cv2.waitKey(0) # waits until interuption by any key

cv2.destroyAllWindows() # closes everything on interuption
