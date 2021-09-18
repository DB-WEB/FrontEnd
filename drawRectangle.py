import win32gui
import win32api
from win32api import GetSystemMetrics
import threading
import keyboard


class ScreemAear:
    def __init__(self):
        self.dc = win32gui.GetDC(0)
        self.monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

        self.red = win32api.RGB(218, 220, 224)  # Red
        self.green = win32api.RGB(0, 0, 255)
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)

    def DrawRectangle(self):
        for x in range(int(self.width)):
            win32gui.SetPixel(self.dc, x, 0, self.red)  # draw red at 0,0
            win32gui.SetPixel(self.dc, x,self.height-2,self.red)  # y,x
        for y in range(self.height):
            win32gui.SetPixel(self.dc, 0, y,self.red)  # draw red at 0,0
            win32gui.SetPixel(self.dc, self.width-2, y, self.red)  # y,x

    def drawFace(self, x, y, w, h):
        for pix in range(w):
            win32gui.SetPixel(self.dc, x+pix , y, self.green)
            win32gui.SetPixel(self.dc, x+pix, h+y, self.green)
        for pix in range(h):
            win32gui.SetPixel(self.dc,x, y+pix, self.green)
            win32gui.SetPixel(self.dc,x+w, y+pix, self.green)
