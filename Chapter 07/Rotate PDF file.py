
import PyPDF2

strFileName = 'Stock Prices.pdf'
strRotatedFileName = 'Stock Prices Rotated File.pdf'
intRotation = 90

objPDF = open(strFileName, 'rb')
objPDFReader = PyPDF2.PdfReader(objPDF)
objPDFWriter = PyPDF2.PdfWriter()
objPage = objPDFReader.pages[0]
objPage.rotate(intRotation)
objPDFWriter.add_page(objPage)
objRotatedFile = open(strRotatedFileName, 'wb')
objPDFWriter.write(objRotatedFile)
objPDF.close()
objRotatedFile.close()
