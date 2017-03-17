#https://pythonprogramming.net/template-matching-python-opencv-tutorial/?completed=/canny-edge-detection-gradients-python-opencv-tutorial/
import cv2
import numpy as np

img_rgb = cv2.imread('chip.jpg')
img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('chipKnot.jpg',0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_grey, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

print('go through matches')
for pkt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pkt, (pkt[0] + w, pkt[1] + h), (0,255,255), 2)

print('finished matches')
cv2.namedWindow('detected', cv2.WINDOW_NORMAL)
cv2.resizeWindow('detected', 650,500)
cv2.imshow('detected', img_rgb)
cv2.waitKey(0)
