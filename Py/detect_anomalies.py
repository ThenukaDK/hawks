import os
import cv2
import time
import datetime
import uuid
import MySQLdb

#connect to DB
db = MySQLdb.connect(host="127.0.0.1",
                     user="root",         
                     passwd="root",  
                     db="windguard")
cur = db.cursor()

log_cascade = cv2.CascadeClassifier("CascadeLogs130x130_10Stages.xml")
cut_cascade = cv2.CascadeClassifier("stage11.xml")


for filename in os.listdir("../img/imagemap"):
    count_logs = 0
    count_cuts = 0
    if filename.endswith("jpg"):

        img = cv2.imread("../img/imagemap/"+filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        logs = log_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in logs:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            count_logs = count_logs+1
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            cuts = cut_cascade.detectMultiScale(roi_gray)
            
            for (ex,ey,ew,eh) in cuts:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
                count_cuts = count_cuts+1
        
        
               
    #rename the file with date and time stamp
    anomalyId = str(uuid.uuid4())
    dateTime =time.strftime("%Y%m%d-%H%M%S")
    new_name = dateTime + anomalyId
    cv2.imwrite("../img/detected_images/"+new_name+".jpg",img)

    #anamolies
    total_anomalies = count_logs + count_cuts
    print (count_logs)
    print (count_cuts)
    print(new_name)

    #send image url to database
    add_image_url = ("INSERT INTO anamolies ""(anomalyId, imageMapId, noOfAnamolies,noOfLogs, noOfCuts, noOfMarijuana, alertSend, imageUrl, dateTime) ""VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_image_url = (anomalyId, '123', total_anomalies,count_logs,count_cuts,'0','0','../img/detected_images/'+new_name+'.jpg', datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
    cur.execute(add_image_url,data_image_url)
    
    
    
db.close()

