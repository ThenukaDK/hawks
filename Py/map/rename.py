import os


def countFiles():
    count = 0
    for filename in os.listdir("././img/aerial"):
         if filename.endswith(".jpg"):
             count = count + 1
    return count

def rename():
    fileCount = countFiles()
    count = 0
    
    for filename in os.listdir("././img/aerial"):
        if filename.endswith(".jpg"):
            newName = 'file'+str(fileCount)+'.jpg'
            os.rename(filename, newName)
        fileCount = fileCount - 1

rename()
