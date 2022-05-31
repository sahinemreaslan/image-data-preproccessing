import cv2
vidcap = cv2.VideoCapture('C:/Users/Emre/Desktop/Yazgit & Aİ2FC/Dataset/OtherDataset/3.mp4')
success,image = vidcap.read()
count = 16305
while success:
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    if(count % 15 == 0):
        cv2.imwrite("frame%d.jpg" % count, image,[cv2.IMWRITE_JPEG_QUALITY, 100])     # save frame as JPEG file      
    count += 1
    
  
print("Count Value : ",count)   
