import rpa as r
r.init()
r.url('https://c4.wallpaperflare.com/wallpaper/734/647/661/quote-motivational-wallpaper-preview.jpg')
r.snap('page', 'Captured_Image.png')
r.wait(5)
r.close()


import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = 'Captured_Image.png'

text = pytesseract.image_to_string(image, lang='eng', config='--psm 11')

print(text)