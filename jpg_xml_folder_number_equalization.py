import glob,os
liste = glob.glob("*.jpg")
liste2 = glob.glob("*.xml")

jpg_dosya_sayisi = len(liste)
xml_dosya_sayisi = len(liste2)
sayac = 1
deger = 0
for i in range(0,jpg_dosya_sayisi):
    liste[i] = liste[i].replace(".jpg","") 

for j in range(0,xml_dosya_sayisi):
    liste2[j] = liste2[j].replace(".xml","")
    
if(jpg_dosya_sayisi > xml_dosya_sayisi):
    print(".jpg, uzantılı dosya sayisi .xml dosya uzantı sayisindan fazladir..")
    for i in range(0,jpg_dosya_sayisi,1):
        for j in range(0,xml_dosya_sayisi,1):   
            if liste[i] == liste2[j]:
                sayac = 0
            elif j == xml_dosya_sayisi-1 and sayac == 1:
                silinicek_jpg = liste[i]
                os.remove(silinicek_jpg+".jpg")
                deger += 1
        sayac = 1
elif(jpg_dosya_sayisi < xml_dosya_sayisi):
    print(".xml, uzantılı dosya sayisi .jpg uzantılı dosya sayisindan fazladir.")
    for i in range(0,xml_dosya_sayisi,1):
        for j in range(0,jpg_dosya_sayisi,1):   
            if liste2[i] == liste[j]:
                sayac = 0
        if sayac == 1:
            silinicek_jpg = liste2[i]
            os.remove(silinicek_jpg+".xml")
        sayac = 1
else:
    print("esit")

        
    
