# Read in the file
import glob,os
dizi = glob.glob("*.xml")
className = '0'
for i in range(0,len(dizi)):
  with open(str(dizi[i]), 'r') as file :
    filedata = file.read()
    while(filedata.find('<object>\n\t\t<name>0') != -1):
        init_value = filedata.find('<object>\n\t\t<name>'+className)
        filedata = filedata[0:init_value]+filedata[init_value+220:]
        print(filedata.find('<object>\n\t\t<name>0'))
        print(filedata.find('<object>\n\t\t<name>0'))
  with open(str(dizi[i]), 'w') as file:
    file.write(filedata)
    
