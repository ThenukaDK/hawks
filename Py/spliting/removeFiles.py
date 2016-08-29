import os

#remove each .avi file in directory specified
def removeFiles():
    for filename in os.listdir("../../img/video/"):
         if filename.endswith(".avi"):
             os.remove("../../img/video/"+str(filename))

#function call
removeFiles()
