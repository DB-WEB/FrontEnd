import win32gui
import win32api
from win32api import GetSystemMetrics
import threading
import keyboard


class ScreemAear:
    def __init__(self):
        self.dc = win32gui.GetDC(0)
        self.monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

        self.red = win32api.RGB(0, 0, 0)  # Red
        self.green = win32api.RGB(0, 255, 0)
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)

    def DrawRectangle(self):
        for x in range(int(self.width/2)):
            win32gui.SetPixel(self.dc, int(self.width/2)+x,
                              0, self.red)  # draw red at 0,0
            win32gui.SetPixel(self.dc, int(self.width/2)+x,
                              int(self.height/2), self.red)  # y,x
        for y in range(int(self.height/2)):
            win32gui.SetPixel(self.dc, int(self.width/2), y,
                              self.red)  # draw red at 0,0
            win32gui.SetPixel(self.dc, self.width-2, y, self.red)  # y,x

    def drawFace(self, x, y, w, h):
        for pix in range(w+40):
            win32gui.SetPixel(self.dc, int(self.width/2) -
                              20 + x+pix, y-20, self.green)
            win32gui.SetPixel(self.dc, int(self.width/2) -
                              20 + x+pix, y+h+20, self.green)
        for pix in range(h+40):
            win32gui.SetPixel(self.dc, int(self.width/2) +
                              x-20, y+pix-20, self.green)
            win32gui.SetPixel(self.dc, int(self.width/2) +
                              x+w+20, y+pix-20, self.green)
