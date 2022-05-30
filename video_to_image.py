
import cv2
vidcap = cv2.VideoCapture('C:/Users/Emre/Desktop/VID_20211109_022216.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image,[cv2.IMWRITE_JPEG_QUALITY, 100)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
