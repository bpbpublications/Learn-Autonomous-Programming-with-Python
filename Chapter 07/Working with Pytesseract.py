import pytesseract
from PIL import Image

img = Image.open('Test_OCR.jpg')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

imagetext = pytesseract.image_to_string(img)

print(imagetext)
