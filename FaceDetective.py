from PIL import ImageGrab
import numpy as np
import cv2
import datetime
import time
import os
import pyautogui

class ScreenVideoControl(object):
    def __init__(self):
        self.fps = 25  # 帧率为25，可以调节
        pyautogui.FAILSAFE =False
        self.video = cv2.VideoWriter(None, cv2.VideoWriter_fourcc(*'XVID'), self.fps,
                                     ImageGrab.grab().size)
        self.face_detection = cv2.CascadeClassifier('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml')

    def run(self):
        self.video_record()
        #self.remove_path_file()
    
    def Det(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        faces =self.face_detection.detectMultiScale(gray, 1.3, 5) 
        for (x,y,w,h) in faces: 
            cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),3) 
            pyautogui.moveTo(x+(w/2),y+(h)/2,duration=1)
            pyautogui.click(x+(w/2),y+(h)/2)
            pyautogui.click(x+(w/2),y+(h)/2)
           
    def video_record(self):
        print("screen record is doing........")
        print('---录屏已经开始了--')
        while True:
            im = ImageGrab.grab()
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR格式
            self.Det(imm)
            
screen_video=ScreenVideoControl()
screen_video.run()




