import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
#set region to black
img[50:100, 50:100] = [0,0,0]
print(img.shape)
print(img.size)
print(img.dtype)
#resize the window
cv2.namedWindow('pic', cv2.WINDOW_NORMAL)
cv2.resizeWindow('pic', 450,500)
#show the window
cv2.imshow('pic', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#https://pythonprogramming.net/image-arithmetics-logic-python-opencv-tutorial/?completed=/image-operations-python-opencv-tutorial/
