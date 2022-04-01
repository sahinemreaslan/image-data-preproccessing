from PIL import Image, ImageEnhance,ImageOps
import random


for i in range(1, 222):
    '''
    if i == 6 or i == 7 or i == 210 or i == 211 or i == 127 or i == 128 or i == 139 or i == 153:
        continue
    else:
        colorImage  = Image.open(r"Ayna/MYVeri"+str(i)+".jpg")
        random_sayi_2 = random.uniform(0.3,3.0)
        colorImage = ImageEnhance.Brightness(colorImage)
        colorImage = colorImage.enhance(random_sayi_2)
        colorImage.save("Ayna/Parlat/MYPVeri"+str(i)+".jpg", quality=100, subsampling=0)
        print(random_sayi_2)
        print("Succes")
    '''
    if i == 6 or i == 7 or i == 210 or i == 211 or i == 127 or i == 128 or i == 139 or i == 153:
        continue
    else:
        colorImage  = Image.open(r"Ayna/MYVeri"+str(i)+".jpg")
        random_sayi_3 = random.uniform(-3,7.0)
        enhance_image = ImageEnhance.Sharpness(colorImage)
        enhance_image = enhance_image.enhance(random_sayi_3)
        enhance_image.save("Ayna/Keskin/KYPVeri"+str(i)+".jpg", quality=100, subsampling=0)
        print(random_sayi_3)
        print("Succes")
    '''
    if i == 6 or i == 7 or i == 210 or i == 211:
        continue
    else:
        colorImage  = Image.open(r"YVeri"+str(i)+".jpg")
        im_mirror = ImageOps.mirror(colorImage)
        im_mirror.save("Ayna/MYVeri"+str(i)+".jpg", quality=100, subsampling=0)
        print("Succes")   

    random_sayi_3 = random.uniform(-3,7.0)
    enhance_image = ImageEnhance.Sharpness(colorImage)
    enhance_image = enhance_image.enhance(-2.0)
    random_sayi_3 = str(random_sayi_3)
    enhance_image.save('3_labeling_enhance'+random_sayi_3+str(a)+'.jpg', quality=100, subsampling=0)
    random_sayi = random.randint(1,330)#1 ile 330 derece arasında
    transposed  = colorImage.rotate(random_sayi)
    random_sayi = str(random_sayi)
    transposed.save('3_labeling_transpose_'+random_sayi+"derece"+str(a)+'.jpg', quality=100, subsampling=0)
    random_sayi_2 = random.uniform(0.3,3.0)
    parlaklik = ImageEnhance.Brightness(colorImage)
    parlaklik = parlaklik.enhance(random_sayi_2)
    random_sayi_2 = str(random_sayi_2)
    parlaklik.save('3_labeling_transpose_'+random_sayi_2+"derece"+str(a)+'.jpg', quality=100, subsampling=0)
    # #üst sınır 3.0
    # #alt sınır 0.30
    print("succes !")
    '''