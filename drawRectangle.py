import win32gui, win32api
from win32api import GetSystemMetrics
import threading
import keyboard

class ScreemAear:
    def __init__(self):
        self.dc = win32gui.GetDC(0)
        self.monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

        self.red = win32api.RGB(255, 0, 0) # Red
        self.width=GetSystemMetrics(0)
        self.height=GetSystemMetrics(1)

    def DrawRectangle(self):
        t1 = threading.Thread(target=self.run)
        t1.start()
        return t1
    
    def run(self):
        while True:
            if keyboard.is_pressed('Esc'):
                break
            for x in range(int(self.width/2)):
                win32gui.SetPixel(self.dc,int(self.width/2)+x,0, self.red)  # draw red at 0,0
                win32gui.SetPixel(self.dc,int(self.width/2)+x,self.height-2 ,self.red)# y,x
            for y in range(int(self.height)):
                win32gui.SetPixel(self.dc,int(self.width/2),y, self.red)  # draw red at 0,0
                win32gui.SetPixel(self.dc,self.width-2,y ,self.red)# y,x


    

