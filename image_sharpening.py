# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:58:50 2020

@author: tanvi
"""

import cv2
import numpy as np

img = cv2.imread("Lenna.png")
cv2.imshow("original",img)
cv2.waitKey(0)

# create our sharpening kernel, we don't normalize since
#the values in the matrix sum to 1

"""
#5x5 kernelsharpens image too much, we have data loss in this case
kernel_sharpening = np.array([[-1,-1,-1,-1,-1],
                              [-1,-1,-1,-1,-1],
                              [-1,-1,25,-1,-1],
                              [-1,-1,-1,-1,-1],
                              [-1,-1,-1,-1,-1]])
"""
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1, 9,-1],
                              [-1,-1,-1]])


# applying different kernel to different image

sharpened = cv2.filter2D(img,-1,kernel_sharpening)

cv2.imshow('sharpened',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
