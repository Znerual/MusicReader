import cv2
import numpy as np

cap = cv2.VideoCapture(0)
minTresh = 60
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retVal, threshold = cv2.threshold(gray, minTresh, 255, cv2.THRESH_BINARY)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('w'):
        minTresh += 5
        minTresh = np.clip(minTresh, 0, 255)
    elif key == ord('s'):
        minTresh -= 5
        minTresh = np.clip(minTresh, 0, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(threshold, str(minTresh) + "current Value", (10, 50), font, 2, (0,0,0),2)
    cv2.imshow('feed',threshold)
cap.release()
cv2.destroyAllWindows()
