# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:59:26 2020

@author: tanvi
"""

import cv2

img = cv2.imread("E:\pyWork\pyProjects\opencv\image1.jpg")

print(img.shape) #image details : height, width,#layers(RGB)

print("Height pixel value :", img.shape[0])
print("Width pixel value :", img.shape[1])
print("Channel value :", img.shape[2])
cv2.imshow('Output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
