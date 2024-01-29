import cv2
import numpy as np


def detect_faces(img):
    grey =cv2.cvtColour(img, cv2.Colour_BGR2GREY)
    faces = face_classifier.detectMultiScale(grey, 1.3, 5)
    if faces == ():
        return img
    

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        return img 
    
    cap =cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = detect_faces(frame)

        cv2.imshow('Video Face Detection', frame)

        if cv2.waitkey(1) & 0xFF == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()