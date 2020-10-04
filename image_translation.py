# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:37:28 2020

@author: tanvi
"""

#image translation or image displacement
 
import cv2
import numpy as np

img =cv2.imread("E:\pyWork\pyProjects\opencv\Lenna.png")
# store height and width of the image
height,width =img.shape[:2]
print(height)
print(width)

quarter_height,quarter_width = height/4,width/4
print(quarter_height)
print(quarter_width)

"""
T= \ 1 0 Tx \
   \ 0 1 Ty \
T is the translation matrix

"""
T = np.float32([[1,0,quarter_width],[0,1,quarter_height]])

print(T)

# we use warpAffine Transformation to shift the image 
# warpAffine : height and width are linear and parallel
#warpNonAffline : titled , non linear image
img_translation = cv2.warpAffine(img,T,(width,height))

cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.imshow("Translation",img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()

