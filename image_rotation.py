# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:37:53 2020

@author: tanvi
"""

import cv2
import numpy as np

img = cv2.imread("E:/pyWork/pyProjects/opencv/opencv/Lenna.png")
height,width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),70, .7)

rotated_image = cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.imshow("Rotated",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
