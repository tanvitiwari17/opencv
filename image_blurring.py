# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:36:56 2020

@author: tanvi
"""

import cv2
import numpy as np

img =cv2.imread("Lenna.png")

cv2.imshow("original",img)
cv2.waitKey(0)

kernel_3x3=np.ones((3,3),np.float32)/9

blurred = cv2.filter2D(img,-1,kernel_3x3)
cv2.imshow("3x3 Kernel Blurred",blurred)
cv2.waitKey(0)

kernel_7x7 = np.ones((7,7),np.float32)/49
blurred2 = cv2.filter2D(img,-1,kernel_7x7)
cv2.imshow("7x7 Kernel Blurred", blurred2)
cv2.waitKey(0)
cv2.destroyAllWindows()
