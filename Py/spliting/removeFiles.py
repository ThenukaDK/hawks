import os


def removeFiles():
    for filename in os.listdir("../../img/video/"):
         if filename.endswith(".avi"):
             os.remove("../../img/video/"+str(filename))

removeFiles()
