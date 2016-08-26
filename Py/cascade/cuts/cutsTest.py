import os
import cv2
import numpy as np

cut_count = 0    
i = 0

cut_cascade = cv2.CascadeClassifier("stage11.xml")


for filename in os.listdir("../../../img/imagemap"):
    if filename.endswith("jpg"):

        img = cv2.imread("../../../img/imagemap/"+filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cuts = cut_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in cuts:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            cut_count = cut_count + 1

    cv2.imwrite("../../../img/detected_images/image"+str(i)+".jpg",img)

    i = i+1

cv2.waitKey(0)

