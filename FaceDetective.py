from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from win32api import *
import os
import pyautogui
import keyboard
from drawRectangle import ScreemAear


class ScreenVideoControl(object):
    def __init__(self):
        self.fps = 25  # 帧率为25，可以调节
        pyautogui.FAILSAFE = False
        self.save_dir = 'C:\\Users\\Administrator\\Desktop\\Matchs\\Vadio'
        self.screen_file_path = None
        self.get_video_path()
        self.screen_width = GetSystemMetrics(0)
        self.screen_height = GetSystemMetrics(1)
        

        self.face_detection = cv2.CascadeClassifier(
            'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml')
        self.video = cv2.VideoWriter(self.screen_file_path, cv2.VideoWriter_fourcc(*'XVID'), self.fps,
                                     ImageGrab.grab(self.getBox()).size)

    def run(self):
        self.video_record()
        # self.remove_path_file()

    # 识别人脸
    def detectFace(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_detection.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            template = cv2.imread('test.jpg')
            self.match_img(img, template, 0.9)
            #pyautogui.moveTo(x+(w/2), y+(h)/2, duration=0.25)
            #pyautogui.click(x+(w/2), y+(h)/2)

    def video_record(self):
        print("screen record is doing........")
        thread = ScreemAear().DrawRectangle()
        while True:
            im = ImageGrab.grab(self.getBox()) #(left_x, top_y, right_x, bottom_y)
            # 转为opencv的BGR格式
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            self.detectFace(imm)
            self.video.write(imm)
            if keyboard.is_pressed('Esc'):
                break
        self.video.release()
        cv2.destroyAllWindows()
        thread.join()

    def get_video_path(self):
        # 录屏保存的文件目录路径
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        # 得到录屏保存的文件路径 按照时间创建文件夹
        file_name = datetime.datetime.now().strftime(
            '%Y-%m-%d %H-%M-%S') + '_screen.avi'
        # 文件路径
        self.screen_file_path = os.path.join(self.save_dir, file_name)
    
    def generate_img_name(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')+'.png'

    #匹配要找得人脸
    def match_img(self, image, template, value):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        w, h = template_gray.shape[::-1]
        res = cv2.matchTemplate(
            gray_image, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >= value:
            top_left = max_loc
            cv2.rectangle(image, top_left,(top_left[0]+w, top_left[1]+h), 255, 2)
            cv2.putText(image,"MR-XIAO-Ming",top_left,cv2.FONT_HERSHEY_SIMPLEX,0.2,(0,0,255))
            cv2.imwrite(self.generate_img_name(), image)
            cv2.imshow(self.generate_img_name(),image)
            cv2.waitKey(0)

    def getBox(self):
        bbox =(self.screen_width/2,0,self.screen_width,self.screen_height)
        return bbox

screen_video = ScreenVideoControl()
screen_video.run()




# corp
# 比如有张图片大小的是100X100,要裁剪其中x=10,y=5,h=20,w=20的就

# img=img[5:25,10:30]
