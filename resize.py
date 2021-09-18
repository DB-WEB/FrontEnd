import cv2
import os
files = os.listdir('ShootCut')
for file in files:
    if(os.path.isfile(os.path.join('ShootCut',file))):
        img=cv2.imread(os.path.join('ShootCut',file),0)
        resize = cv2.resize(img,(100,100),interpolation=cv2.INTER_AREA)



