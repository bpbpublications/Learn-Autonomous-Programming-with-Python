import PyPDF2

listPDFs = ['Stock Prices.pdf', 'Stock Prices Rotated File.pdf']
strMergedFileName = 'Stock Prices Merged File.pdf'
objPDFMerger = PyPDF2.PdfMerger()

for objPDF in listPDFs:
    objPDFMerger.append(objPDF)

objPDFMerger.write(open(strMergedFileName, 'wb'))
   
