import cv2
import numpy as np

countLogs = 0

logs_cascade = cv2.CascadeClassifier("CascadeLogs130x130_10Stages.xml")

img = cv2.imread('frame640.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


logs = logs_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in logs:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    countLogs = countLogs + 1


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',800,600)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
