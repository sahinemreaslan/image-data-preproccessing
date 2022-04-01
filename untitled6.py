import os
  



for i in range(1,222):
# Source file path
    if i == 6 or i == 7 or i == 210 or i == 211:
        continue
    else:
    
        source = "Keskin/YVeri"+str(i)+".xml"
    
        # destination file path
        dest = "Keskin/KYVeri"+str(i)+".xml"
          
          
        # Now rename the source path
        # to destination path
        # using os.rename() method
        os.rename(source, dest)
        print("Source path renamed to destination path successfully.")