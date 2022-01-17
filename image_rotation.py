from PIL import Image



'''
colorImage  = Image.open("C:/Users/Emre/Desktop/1/IMG_"+"1"+".jpg")
transposed  = colorImage.transpose(Image.ROTATE_270)
transposed.show()


'''
for a in range(1, 1107, 1):
    if a%5==0:
        continue
    elif a%2==0:    
        colorImage  = Image.open("C:/Users/Emre/Desktop/Yeni_HQ_Dataset/IMG_"+str(a)+".jpg")
        #transposed  = colorImage.transpose(Image.ROTATE_270)
        colorImage.save('3_labeling'+str(a)+'.jpg')
        print("succes !")