# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:03:26 2020

@author: tanvi
"""
import cv2
import numpy as np

square = np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-1) # -1 to fill
cv2.imshow('Square',square)
cv2.waitKey(0)

# making an ellipse
ellipse=np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("Ellipse",ellipse)
cv2.waitKey()

# bitwise and
And = cv2.bitwise_and(square,ellipse)
cv2.imshow("AND",And)
cv2.waitKey(0)

# bitwise or
Or = cv2.bitwise_or(square,ellipse)
cv2.imshow("OR",Or)
cv2.waitKey(0)

# bitwise xor
Xor = cv2.bitwise_xor(square,ellipse)
cv2.imshow("XOR",Xor)
cv2.waitKey(0)

# bitwise and
Not = cv2.bitwise_not(ellipse)
cv2.imshow("NOT",Not)
cv2.waitKey(0)


cv2.destroyAllWindows()
