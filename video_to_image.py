import cv2
vidcap = cv2.VideoCapture('C:/Users/Emre/Desktop/Dataset\TrainDataset/20.mp4')
success,image = vidcap.read()
count = 14846
while success:
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    if(count % 3 == 0):
        cv2.imwrite("frame%d.jpg" % count, image,[cv2.IMWRITE_JPEG_QUALITY, 100])     # save frame as JPEG file      
    count += 1
    
  
print("Count Value : ",count)   
