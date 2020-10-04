# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:51:54 2020

@author: tanvi
"""

import cv2

img = cv2.imread('E:\pyWork\pyProjects\opencv\image1.jpg')

cv2.imshow("Original Image",img)

cv2.imwrite('Output.jpg',img) # creates a clone of img 
cv2.imwrite('Output.png',img)
cv2.waitKey(0)

cv2.destroyAllWindows()