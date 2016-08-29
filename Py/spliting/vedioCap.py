import cv2
import numpy as np
import os

#get file names listed in vedio directory
def getFileNames():
    fileCount = countFiles()

    fileArray = []
    
    for filename in os.listdir("../../img/video/"):
        if filename.endswith(".avi"):
            fileArray.append(filename)                
        fileCount = fileCount - 1

    return fileArray

#count number of avi files inside directory
def countFiles():
    count = 0
    for filename in os.listdir("../../img/video/"):
         if filename.endswith(".avi"):
             count = count + 1
    return count

#execute getfiles method 
files = getFileNames()

count = 0

#for each .avi file in directory splitt vedios into frames
for filename in files:

    location = "../../img/video/"+str(filename)
    vidcap = cv2.VideoCapture(location)
    success,image = vidcap.read()
    print success

    while success:
        success,image = vidcap.read()

        getvalue = vidcap.get(0)
        print "get value = "+str(getvalue)
        print "count id = "+str(count)

        if count%20 == 0:
            cv2.imwrite("../../img/aerial/frame%d.jpg" %count, image)

        if cv2.waitKey(10) == 27:                     
            break
        count += 1
       

