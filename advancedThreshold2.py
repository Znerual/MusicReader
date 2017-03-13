#could implenet controll from threshold.py

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('feed', threshold)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
