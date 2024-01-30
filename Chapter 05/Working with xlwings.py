import xlwings as xlw
obj_excel_app = xlw.App(visible=False)
objWorkbook = xlw.Book('Student Table.xlsx') 
objWorksheet = objWorkbook.sheets[0]
formula = '=ROUND(AVERAGE(B2:F2),0)'
objWorksheet.range("G2,G3,G4").formula = formula
objWorkbook.save()
objWorkbook.close()
obj_excel_app.kill()
