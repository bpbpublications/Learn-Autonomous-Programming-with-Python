import PyPDF2
pdfReader = PyPDF2.PdfReader('Stock Prices.pdf')  
pageObj = pdfReader.pages[0]
print(pageObj.extract_text())







