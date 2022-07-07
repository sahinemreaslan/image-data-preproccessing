import glob,os,re
import PIL
import os
import os.path
from PIL import Image
dizi = glob.glob("*.xml")

i = 0
width = []
height = []
f = r'C:/Users/sahin/Desktop/VERİSETİ/a/images'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    width.append(img.width)
    height.append(img.height)
    i+=1


for i in range(0,len(dizi)):
  with open(str(dizi[i]), 'r') as file :
    filedata = file.read()
    start = filedata.find("<width>")
    finish = filedata.find("</width>") 
    filedata = filedata[:start+7] + str(width[i]) + filedata[finish:]

    start = filedata.find("<height>")
    finish = filedata.find("</height>")
    filedata = filedata[:start+8] + str(height[i]) + filedata[finish:]
    
    

  with open(str(dizi[i]), 'w') as file:
    file.write(filedata)
