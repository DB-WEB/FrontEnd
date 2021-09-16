import cv2

img=cv2.imread('1365470-20190325202348896-1685286902.png',0)
w=24
h=24
resize = cv2.resize(img,(w,h),interpolation=cv2.INTER_AREA)
cv2.imshow('size',resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

