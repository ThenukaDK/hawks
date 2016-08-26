import os
import cv2
import numpy as np

cut_count = 0    
i = 0

log_cascade = cv2.CascadeClassifier("CascadeLogs130x130_10Stages.xml")


for filename in os.listdir("../../../img/detected_images"):
    if filename.endswith("jpg"):

        img = cv2.imread("../../../img/detected_images/"+filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        logs = log_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in logs:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cut_count = cut_count + 1

    cv2.imwrite("../../../img/detected_images/"+filename,img)

    i = i+1

cv2.waitKey(0)

