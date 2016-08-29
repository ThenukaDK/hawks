from panorama import Stitcher
import imutils
import cv2
import os
import time
import datetime
import uuid
import MySQLdb

#connect to DB
db = MySQLdb.connect(host="127.0.0.1",
                     user="root",         
                     passwd="root",  
                     db="windguard")

#start database cursor
cur = db.cursor()

#count .jpg files in specified directory
def countFiles():
    nameArray = []
    count = 0
    for filename in os.listdir("../../img/aerial/"):
         if filename.endswith(".jpg"):
             nameArray.append("../../img/aerial/"+str(filename))
             count = count + 1
    return count, nameArray

#function call to count files
fileCount, names = countFiles()

#get 4 files each and stich 
for i in range(0,fileCount,4):
    imageA = cv2.imread(names[i])
    imageB = cv2.imread(names[i+1])
    imageC = cv2.imread(names[i+2])
    imageD = cv2.imread(names[i+3])

    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result2, vis2) = stitcher.stitch([imageC, imageD], showMatches=True)

    imageE = result
    imageF = result2
    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result3, vis3) = stitcher.stitch([imageE, imageF], showMatches=True)

    #rename the file with date and time stamp
    anomalyId = str(uuid.uuid4())
    notificationId = str(uuid.uuid4())
    dateTime =time.strftime("%Y%m%d-%H%M%S")
    new_name = dateTime + anomalyId
    cv2.imwrite("../../img/imagemap/"+new_name+".jpg",result3)

    #send image url to database
    add_image_url = ("INSERT INTO image_map ""(imageMapId, poleId, copterId, longitude, latitude, imageUrl, dateTime) ""VALUES (%s, %s, %s, %s, %s, %s, %s)")
    data_image_url = (anomalyId, '123'+str(i), i, '85.55','6.35', "../../img/imagemap/"+new_name+".jpg" ,datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
    cur.execute(add_image_url,data_image_url)

cv2.waitKey(0)




