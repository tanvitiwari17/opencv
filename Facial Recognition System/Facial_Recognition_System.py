# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:25:46 2020

@author: tanvi
"""

# importing libraries

import cv2
import numpy as np

# to extract face features

face_classifier = cv2.CascadeClassifier('C:/Users/tanvi/.conda/pkgs/opencv-3.3.1-py36h20b85fd_1/Library/etc/haarcascades/haarcascade_frontalface_default.xml' ) 



def face_extractor(img):
    
    # converting image to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # multiscaling,fixing scaling value and  neighbouring value
    
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    
    # cropping face
    
    if faces is():
        return None
    
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h,x:x+w]
        
    return cropped_face
    
    
    # open webcam
    
cap = cv2.VideoCapture(0)
count = 0

    # start reading 

while True:
    ret,frame = cap.read()
    
    # if face extraction has a value, counter starts, resizing and taking the pictue and saving it to given path.
    
    if face_extractor(frame) is not None:
        
        count+=1
        
        # resizing frame
        
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        
        # saving values
        
        file_name_path = 'E:/pyWork/pyProjects/opencv/face_recog/user' + str(count)+ '.jpg'
        cv2.imwrite(file_name_path,face)
    
        # counter : putText(where,count,position pointer, font,font scale,RGB color,thickness)
    
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        # to show
        
        cv2.imshow('Face Cropper', face)
    
    else:
        print("Face not Found")
        pass
    
    if cv2.waitKey(1)==13 or count ==100: 
        break

cap.release()
cv2.destroyAllWindows()
print("Sample Collection is Complete!!")
      
    
    
