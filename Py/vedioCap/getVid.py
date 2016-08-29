import cv2
import time

count = 0

# find the webcam
capture = cv2.VideoCapture(0)

w=int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))

# video recorder
fourcc = cv2.cv.CV_FOURCC(*'XVID')  
video_writer = cv2.VideoWriter("../../img/video/output.avi", fourcc, 8, (w, h)) 

def waitSeconds():
    time.sleep(1)

    

# record video
while (capture.isOpened()):
    ret, frame = capture.read()
    count = count +1
    print count
    if ret and count<100:
        video_writer.write(frame)
    else:
        break

capture.release()
video_writer.release()
cv2.destroyAllWindows()
