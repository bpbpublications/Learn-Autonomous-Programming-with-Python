
from img2table.document import PDF
from img2table.ocr import TesseractOCR

obj_pdf = PDF(src="Stock Prices.pdf")

obj_ocr = TesseractOCR(lang="eng")

obj_pdf_tables = obj_pdf.extract_tables(ocr=obj_ocr)

obj_pdf.to_xlsx("Extracted_Tables.xlsx", ocr=obj_ocr)
