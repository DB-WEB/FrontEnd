from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from win32api import *
import os
import pyautogui
import keyboard
from drawRectangle import ScreemAear
from tkinter import *


class ScreenVideoControl(object):
    def __init__(self):
        self.fps = 10  # 帧率为25，可以调节
        pyautogui.FAILSAFE = False
        self.save_dir = 'Vadio'
        self.imgCut = 'ShootCut'
        self.screen_file_path = None
        self.get_video_path()
        self.screen_width = GetSystemMetrics(0)
        self.screen_height = GetSystemMetrics(1)
        self.ScreemAear = ScreemAear()
        self.threadContainer = []
        self.face_detection = cv2.CascadeClassifier('cascade.xml')
        self.video = cv2.VideoWriter(self.screen_file_path, cv2.VideoWriter_fourcc(*'XVID'), self.fps,
                                     ImageGrab.grab(self.getBox()).size)

    def run(self):
        self.video_record()

        # self.remove_path_file()

    # 识别人脸
    def detectFace(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        faces = self.face_detection.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            self.ScreemAear.drawFace(x, y, w, h)
            files = os.listdir(self.imgCut)
            crop = img[y:h+y, x:w+x]
            if(len(files) == 0):
                cv2.imwrite(os.path.join(
                    self.imgCut, self.generate_img_name()), crop)
            maxScore = 0
            # 找到最像得那种照片
            files = os.listdir(self.imgCut)
            for file in files:
                if os.path.isfile(os.path.join(self.imgCut, file)):
                    template = cv2.imread(os.path.join(self.imgCut, file))
                    score = self.match_img(crop, template)
                    if(score > maxScore):
                        maxScore = score
            if(maxScore < 0.8):
                filename = self.generate_img_name()
                print("找到新目标 %s", filename)
                cv2.imwrite(os.path.join(self.imgCut, filename), crop)

            #template = cv2.imread('test.jpg')
            #self.match_img(img, template, 0.9)
            #pyautogui.moveTo(x+(w/2), y+(h)/2, duration=0.25)
            #pyautogui.click(x+(w/2), y+(h)/2)

    def video_record(self):
        print("screen record is doing........")
        while True:
            # (left_x, top_y, right_x, bottom_y)
            im = ImageGrab.grab(self.getBox())
            # 转为opencv的BGR格式
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            self.detectFace(imm)
            self.video.write(imm)
            self.ScreemAear.DrawRectangle()
            if keyboard.is_pressed('Esc'):
                break
        self.video.release()
        cv2.destroyAllWindows()

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

    # 人脸是否存在
    def match_img(self, image, template):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        w, h = template_gray.shape[::-1]
        res = cv2.matchTemplate(
            gray_image, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return max_val

    def getBox(self):
        #bbox = (self.screen_width/2, 0, self.screen_width, self.screen_height/2)
        bbox = (0, 0, self.screen_width, self.screen_height)
        return bbox


screen_video = ScreenVideoControl()
screen_video.run()


# corp
