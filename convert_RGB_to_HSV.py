# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:53:02 2020

@author: tanvi
"""

# HSV color space : Hue, Saturation,Value
# H - 0 to 180 deg  ; 0 - 180
# V - to 1/2  : 0 - 255
# S - to 1    : 0 - 255

import cv2

img = cv2.imread("E:\pyWork\pyProjects\opencv\Lenna.png")

img_HSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.imshow("HSV Image", img_HSV)
cv2.imshow("Hue Channel",img_HSV[:,:,0])
cv2.imshow("Saturation Channel",img_HSV[:,:,1])
cv2.imshow("Value Channel",img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()
