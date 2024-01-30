import xlsxwriter as xr
objWorkbook = xr.Workbook('Learn_Writer.xlsx')
objWorksheet = objWorkbook.add_worksheet('Exercise')
objWorksheet.write('A1','This is my first tutorial in xlsxwriter!')
objWorkbook.close()
