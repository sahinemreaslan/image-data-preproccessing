from PIL import Image, ImageEnhance
import random


for a in range(1, 1107, 5):
    colorImage  = Image.open(r"C:/Users/Emre/Desktop/Yeni_HQ_Dataset_Sadece Beyaz/IMG_"+str(a)+".jpg")
    colorImage = ImageEnhance.Brightness(colorImage)
    colorImage = colorImage.enhance(1)
    colorImage.save("IMG_"+str(a)+".jpg")
	bulanıklık ve keskinlik
    random_sayi_3 = random.uniform(-3,7.0)
    enhance_image = ImageEnhance.Sharpness(colorImage)
    enhance_image = enhance_image.enhance(-2.0)
    random_sayi_3 = str(random_sayi_3)
    enhance_image.save('3_labeling_enhance'+random_sayi_3+str(a)+'.jpg', quality=100, subsampling=0)
    	döndürme
    random_sayi = random.randint(1,330)#1 ile 330 derece arasında
    transposed  = colorImage.rotate(random_sayi)
    random_sayi = str(random_sayi)
    transposed.save('3_labeling_transpose_'+random_sayi+"derece"+str(a)+'.jpg', quality=100, subsampling=0)
	parlaklıkkkk
    random_sayi_2 = random.uniform(0.3,3.0)
    parlaklik = ImageEnhance.Brightness(colorImage)
    parlaklik = parlaklik.enhance(random_sayi_2)
    random_sayi_2 = str(random_sayi_2)
    parlaklik.save('3_labeling_transpose_'+random_sayi_2+"derece"+str(a)+'.jpg', quality=100, subsampling=0)
    # #üst sınır 3.0
    # #alt sınır 0.30
    print("succes !")
