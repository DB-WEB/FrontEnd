from PIL import ImageGrab
import numpy as np
import cv2
import datetime
import time
import os
import pyautogui
import keyboard

class ScreenVideoControl(object):
    def __init__(self):
        self.fps = 25  # 帧率为25，可以调节
        pyautogui.FAILSAFE = False
        self.save_dir='D:\\etc'
        self.screen_file_path = None
        self.get_video_path()
      
        self.face_detection = cv2.CascadeClassifier(
            'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml')
        self.video = cv2.VideoWriter(self.screen_file_path,cv2.VideoWriter_fourcc(*'XVID'), self.fps,
                                     ImageGrab.grab().size)

    def run(self):
        self.video_record()
        # self.remove_path_file()

    def moveToFaceAndShoot(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_detection.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 1)
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'####',(x, y-10),font,0.5,(0,0,255),1)
           
           # 记录人脸信息
            ccropped = img[y-20:h+y+20, x-20:w+x+20]
            cv2.imwrite(self.generate_img_name(),ccropped)

            #pyautogui.moveTo(x+(w/2), y+(h)/2, duration=0.25)
            #pyautogui.click(x+(w/2), y+(h)/2)

    def video_record(self):
        print("screen record is doing........")
        while True:
            im = ImageGrab.grab()
            # 转为opencv的BGR格式
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            self.moveToFaceAndShoot(imm)
            self.video.write(imm)
            if keyboard.is_pressed('Esc'):
                break
        self.video.release()
        cv2.destroyAllWindows()

    def get_video_path(self):
        # 录屏保存的文件目录路径
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        # 得到录屏保存的文件路径 按照时间创建文件夹
        file_name = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '_screen.avi'
        # 文件路径
        self.screen_file_path = os.path.join(self.save_dir, file_name)

    def generate_img_name(self):
        return  datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')+'.png'

screen_video = ScreenVideoControl()
screen_video.run()


#corp
#比如有张图片大小的是100X100,要裁剪其中x=10,y=5,h=20,w=20的就

#img=img[5:25,10:30]
