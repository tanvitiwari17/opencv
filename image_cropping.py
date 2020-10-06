# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:12:49 2020

@author: tanvi
"""
import cv2

img = cv2.imread("Lenna.png")

height,width = img.shape[:2]

# starting pixel coordinates(top left, of cropping rect)
start_row,start_col = int(height*.25),int(width*.25)

# ending pixel coordinates (bottom right)
end_row,end_col = int(height*.75),int(width*.75)

cropped = img[start_row:end_row,start_col:end_col]

cv2.imshow("Original",img)
cv2.waitKey(0)

cv2.imshow("Cropped",cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()