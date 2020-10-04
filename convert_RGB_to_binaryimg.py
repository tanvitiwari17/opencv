# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:29:49 2020

@author: tanvi
"""

# binary image -> black(0) and white(1) image
import cv2

#first converting the RGB image to grayscale for simplification

img =cv2.imread("E:\pyWork\pyProjects\opencv\image1.jpg",0)
cv2.imshow("Gray",img)

cv2.waitKey(0)

# creating threshold
# ret stors the return value in form of tuple
ret,b_w = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# values <=127 : black, 127<values<=255 : white

cv2.imshow("Binary Image",b_w)
cv2.waitKey(0)


cv2.destroyAllWindows()
