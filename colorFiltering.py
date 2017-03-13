#https://pythonprogramming.net/color-filter-python-opencv-tutorial/?completed=/thresholding-image-analysis-python-opencv-tutorial/
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([75,60,25])
    upper_green = np.array([130, 100,100])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    img = cv2.bitwise_and(frame, frame, mask= mask)
    cv2.imshow('feed', img)
    cv2.imshow('original', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
