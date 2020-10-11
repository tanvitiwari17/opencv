# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:25:46 2020

@author: tanvi
"""

import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('C:/Users/tanvi/.conda/pkgs/opencv-3.3.1-py36h20b85fd_1/Library/etc/haarcascades/haarcascade_frontalface_default')

def face_extractor(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    
    if faces is():
        return None
    
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h,x:x+w]
        
    return cropped_face
    
    
    
    
cap = cv2.VideoCapture(0)
count =0

while True:
    ret,frame = cap.read()
    
