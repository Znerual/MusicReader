#https://pythonprogramming.net/morphological-transformation-python-opencv-tutorial/?completed=/blurring-smoothing-python-opencv-tutorial/
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_boundary = np.array([0,0,00])
    upper_boundary = np.array([40, 40, 100])

    mask = cv2.inRange(frame, lower_boundary, upper_boundary)
    img = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5,5), np.uint8)

    erosion = cv2.erode(img, kernel, iterations = 1) #bei img bekomme ich ein farbiges bild, bei mask nur ein schwarz weiß
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('original', img)
    cv2.imshow('feed', frame)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
