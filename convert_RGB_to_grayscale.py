# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:17:26 2020

@author: tanvi
"""

import cv2
"""
img = cv2.imread("E:\pyWork\pyProjects\opencv\image1.jpg")

cv2.imshow("Original",img)
cv2.waitKey(0)

# to covert into grayscale:
#method 1
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows() """

# method 2
img = cv2.imread("E:\pyWork\pyProjects\opencv\image1.jpg",0)

cv2.imshow("Gray Scale image",img)

cv2.waitKey(0)
cv2.destroyAllWindows() 