import cv2
count = 0
sayac = 0
for i in range(1,21):
    vidcap = cv2.VideoCapture('C:/Users/Emre/Desktop/Train/Temizlenmiş/1 ('+str(i)+').mp4')
    success,image = vidcap.read()
    while success:
        success,image = vidcap.read()
        #print('Read a new frame: ', success)
        if(count % 3 == 0):
            cv2.imwrite("frame%d_train.jpg" % sayac, image,[cv2.IMWRITE_JPEG_QUALITY, 100])     # save frame as JPEG file      
            sayac+=1 
        count += 1
    print("Count Value : ",count)
