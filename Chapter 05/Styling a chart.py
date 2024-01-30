import openpyxl
from openpyxl import load_workbook 
from openpyxl.chart import BarChart,Reference
from openpyxl.chart.layout import Layout, ManualLayout
objWorkbook = openpyxl.load_workbook('Student Table.xlsx')
objWorksheet = objWorkbook.worksheets[0]
chart = objWorksheet._charts[0]
chart.style = 8
chart.x_axis.title = 'Students'
chart.y_axis.title = 'Scores'
chart.legend.position = 'tr'
chart.title = "Average Scores of Students"
objWorkbook.save("Student Table.xlsx")
