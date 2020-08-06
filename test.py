# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:09:23 2020

@author: nrdas
"""
import numpy as np
import cv2
from livenessmodel import get_liveness_model



input_vid = []
print('Start Recognition!')
prevTime = 0
video_capture = cv2.VideoCapture(0)
video_capture.set(3, 640)
video_capture.set(4, 480)
kmodel = get_liveness_model()
kmodel.load_weights("live_model\\live_model.h5")
pred = [[0]]
while True:
    ret, frame = video_capture.read()
    liveimg = cv2.resize(frame, (100,100))
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)    #resize frame (optional)
            
    if len(input_vid) < 24:
        liveimg = cv2.cvtColor(liveimg, cv2.COLOR_BGR2GRAY)
        input_vid.append(liveimg)
    else:
        liveimg = cv2.cvtColor(liveimg, cv2.COLOR_BGR2GRAY)
        input_vid.append(liveimg)
        inp = np.array([input_vid[-24:]])
        inp = inp/255
        inp = inp.reshape(1,24,100,100,1)
        pred = kmodel.predict(inp)
        #input_vid = input_vid[-25:]
        input_vid = input_vid[-5:]
            
    if pred[0][0] > 0.5:
        print('fake person tho')
        print(pred[0][0])
        continue
    
    print('real_person', pred[0][0])
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        video_capture.release()
        cv2.destroyAllWindows()
        break