#Run each of these pieces of code separately

from PIL import Image
objImage = Image.open("Van.jpg")
fltWidth,fltHeight = objImage.size
print(fltWidth,fltHeight)


from PIL import Image
objImage = Image.open("Van.jpg")
fltWidth,fltHeight = objImage.size
fltArea = (fltWidth/3-100, fltHeight/6, 2*fltWidth/3+100, fltHeight/3)
objImage = objImage.crop(fltArea)
objImage.save("Van-Cropped.jpg")


import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
objImage = Image.open("Van-Cropped.jpg")
imagetext = pytesseract.image_to_string(objImage,config='--psm 7')
print(imagetext)
