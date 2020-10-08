# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:57:37 2020

@author: tanvi
"""

import cv2 
import numpy as np

img=cv2.imread("Lenna.png",0)

height,width = img.shape[:2]

#extract slop edges
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)

cv2.imshow("Original",img)
cv2.waitKey(0)

cv2.imshow("Sobel x Image",sobel_x)
cv2.waitKey(0)

cv2.imshow("Sobel y Image",sobel_y)
cv2.waitKey(0)

Or = cv2.bitwise_or(sobel_x,sobel_y)

cv2.imshow("OR Image",Or)
cv2.waitKey(0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Laplacian Image",laplacian)
cv2.waitKey(0)

# canny edge uses gradient values as threshold
canny= cv2.Canny(img,50,170)
cv2.imshow("Canny Edge",canny)
cv2.waitKey(0)


cv2.destroyAllWindows()