
from pdf2image import convert_from_path
import pytesseract
 
str_pdf_path = "Stock Prices.pdf"

images = convert_from_path(str_pdf_path)
 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

text_output = ''
for image in images:
    text = pytesseract.image_to_string(image)
    text_output += text + '\n'
 

print(text_output)
