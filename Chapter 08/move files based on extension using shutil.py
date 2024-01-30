
import os
import shutil

if not os.path.exists('Images'):
    os.mkdir('Images')
    
for objFile in os.listdir():
    if '.jpg' in objFile.lower():
        strPath = 'Images/'+ objFile
        shutil.move(objFile, strPath) 

