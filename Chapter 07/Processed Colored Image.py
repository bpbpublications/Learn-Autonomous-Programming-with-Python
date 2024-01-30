import pytesseract
from PIL import Image

img = Image.open('Colored_Image_OCR.jpg')
img = img.convert('L')
img = img.save('Processed_Colored_Image_OCR.jpg') 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
imagetext = pytesseract.image_to_string(Image.open('Processed_Colored_Image_OCR.jpg'))
print(imagetext)
