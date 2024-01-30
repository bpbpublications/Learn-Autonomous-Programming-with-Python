from openpyxl import Workbook  

objWorkbook = Workbook() 
 
objWorksheet = objWorkbook.worksheets[0]  
  
objWorksheet.cell(1,1,'This is my first task using Openpyxl') 
 
objWorkbook.save("Learn_Excel_Automation.xlsx")  


