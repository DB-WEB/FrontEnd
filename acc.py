import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('img.jpg', 0)
template = cv.imread('template.jpg', 0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
if max_val>0.5:
    top_left = max_loc
    cv.rectangle(img, top_left, (top_left[0]+w, top_left[1]+h),255,4)
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle("")
    plt.show()


