import cv2
import numpy as np

new_capture = cv2.VideoCapture('mp4file.mp4')

if(new_capture.isOpened() == False):
    print("Error for opening the video file")

while (new_capture.isOpened()):
    ret, frame = new_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

new_capture.release()
cv2.destroyAllWindows()
