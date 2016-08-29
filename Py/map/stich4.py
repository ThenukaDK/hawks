from panorama import Stitcher
import imutils
import cv2
import os


def countFiles():
    nameArray = []
    count = 0
    for filename in os.listdir("../../img/aerial/"):
         if filename.endswith(".jpg"):
             nameArray.append("../../img/aerial/"+str(filename))
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
    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result3, vis3) = stitcher.stitch([imageE, imageF], showMatches=True)

    cv2.imwrite("../../img/imagemap/4stichedimages"+str(i)+".jpg", result3)

cv2.waitKey(0)


