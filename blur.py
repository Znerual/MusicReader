import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([80,60,5])
    upper_green = np.array([130,100,100])

    mask = cv2.inRange(frame, lower_green, upper_green)
    img = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(img, -1, kernel)

    blur = cv2.GaussianBlur(img, (15,15),0)

    median = cv2.medianBlur(img, 15)

    bilateral = cv2.bilateralFilter(img, 15,75,75)

    cv2.imshow('blured',bilateral) #or show smoothened, or blur, or median
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
