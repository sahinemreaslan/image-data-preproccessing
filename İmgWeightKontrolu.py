# Read in the file
import glob,os
dizi = glob.glob("*.xml")
className = '0'
for i in range(0,len(dizi)):
  with open(str(dizi[i]), 'r') as file :
    filedata = file.read()
    if filedata.find("<height>0") != -1 or filedata.find("<width>0") != -1:
        print(dizi[i])
  with open(str(dizi[i]), 'w') as file:
    file.write(filedata)
        