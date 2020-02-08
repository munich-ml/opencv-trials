# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:52:30 2020

@author: holge
"""
import cv2
import datetime as dt



class FpsMeasurement():
    """Class for measuring frames per second"""
    def __init__(self):
        self.t0 = dt.datetime.now()
    
    def measure(self):
        t = dt.datetime.now()
        fps = int(1 / (t - self.t0).total_seconds())
        self.t0 = t
        return "{} fps".format(fps)


cap = cv2.VideoCapture(0)
fps = FpsMeasurement()

while cv2.waitKey(1) == -1:    # while loop exited if any key is pressed
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)    
    edge = cv2.Canny(frame,100,100)
    text = fps.measure()
    cv2.putText(frame, text, (5, 30), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
    cv2.imshow('Original',frame)
    cv2.imshow('Edges Canny', edge)


cv2.destroyAllWindows()
cap.release()