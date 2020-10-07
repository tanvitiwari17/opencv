# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:44:52 2020

@author: tanvi
"""

import cv2
import numpy as np

img = cv2.imread("Lenna.png")
cv2.imshow("Original",img)
cv2.waitKey(0)

# averaging done by convolving the image with a normalize box filter
# This takes the pixel under the box and replace the central element 
# box size needs to be odd and positive

blur = cv2.blur(img,(3,3))
cv2.imshow("Blue image",blur)
cv2.waitKey(0)

# using gaussian kernel
gaussian = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gaussian Blur",gaussian)
cv2.waitKey(0)

# take median of all the pixels under kernel are and central element is replaced with this median value

median = cv2.medianBlur(img,5)
cv2.imshow("Median Blur",median)
cv2.waitKey(0)

# bilateral is very effictive in nose removal
bilateral = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Bilateral Blur",bilateral)
cv2.waitKey(0)


cv2.destroyAllWindows()

