import openpyxl

wb=openpyxl("C:\\Users\\wissem\\Desktop\\BX-Books.xlsx")
sheets=wb.sheetnames
sh1=wb['']
data=sh1['b2'].value
print(data)
