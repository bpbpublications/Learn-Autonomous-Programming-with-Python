
from tabula import read_pdf
objTable = read_pdf("Stock Prices.pdf",pages="all") 
df = objTable[0]
df.to_excel("Stock Prices.xlsx",index=None)
