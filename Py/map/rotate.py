import os
import cv2
import numpy as np

count = 0

#imageOriginal = cv2.imread('frame7560.jpg')

def rotateImage(image, angel):#parameter angel in degrees
    height = image.shape[0]
    width = image.shape[1]
    height_big = height * 2
    width_big = width * 2
    image_big = cv2.resize(image, (width_big, height_big))
    image_center = (width_big/2, height_big/2)#rotation center
    rot_mat = cv2.getRotationMatrix2D(image_center,angel, 0.5)
    result = cv2.warpAffine(image_big, rot_mat, (width_big, height_big), flags=cv2.INTER_LINEAR)
    wrapAfine = np.rot90(image)
    return wrapAfine



for filename in os.listdir("../../img/aerial"):
    if filename.endswith("jpg"):
        imageOriginal = cv2.imread(filename)
        imageRotated= rotateImage(imageOriginal, 90)
        cv2.imwrite(filename, imageRotated)
        cv2.waitKey()
