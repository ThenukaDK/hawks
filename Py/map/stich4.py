from panorama import Stitcher
import numpy as np
import imutils
import cv2
import os


def countFiles():
    nameArray = []
    count = 0
    for filename in os.listdir("../../img/aerial"):
         if filename.endswith(".jpg"):
             nameArray.append(filename)
             count = count + 1
    return count, nameArray


fileCount, names = countFiles()



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

    #merging two results

    height, width, channels = imageE.shape
    #create a null image using numpy with all zeros with diemnetions = 4*width
    blank_image = np.zeros((height,width*2,channels), np.uint8)
    
    blank_image[:,0:width] = imageE    
    blank_image[:,width:width*2] = imageF
    

    cv2.imwrite("../../img/aerial/imagemap/4stichedimages"+str(i)+".jpg", blank_image)

cv2.waitKey(0)

