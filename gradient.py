import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_boundary = np.array([10,10,0])
    upper_boundary = np.array([70,70,100])

    mask = cv2.inRange(hsv, lower_boundary, upper_boundary)
    img = cv2.bitwise_and(frame, frame, mask=mask)

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1,0,ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 50,50) #kleinere werte finden mehr kanten

    cv2.imshow('lap', laplacian)
    cv2.imshow('sobel', sobelx)
    cv2.imshow('edges', edges)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
