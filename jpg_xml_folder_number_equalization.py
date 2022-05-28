import glob,os
liste = glob.glob("*.jpg")
liste2 = glob.glob("*.xml")

jpg_dosya_sayisi = len(liste)
xml_dosya_sayisi = len(liste2)

if(jpg_dosya_sayisi > xml_dosya_sayisi):
    print(".jpg, uzantılı dosya sayisi .xml dosya uzantı sayisindan fazladir..")
else:
    print(".xml, uzantılı dosya sayisi .jpg uzantılı dosya sayisindan fazladir.")
    print("lutfen duzeltin")
    exit(0)

        
for i in range(0,jpg_dosya_sayisi):
    liste[i] = liste[i].replace(".jpg","") 

for j in range(0,xml_dosya_sayisi):
    liste2[j] = liste2[j].replace(".xml","")
    
sayac = 1
deger = 0
for i in range(0,jpg_dosya_sayisi,1):
    for j in range(0,xml_dosya_sayisi,1):   
        if liste[i] == liste2[j]:
            sayac = 0
        elif j == xml_dosya_sayisi-1 and sayac == 1:
            silinicek_jpg = liste[i]
            os.remove(silinicek_jpg+".jpg")
            deger += 1
    sayac = 1
