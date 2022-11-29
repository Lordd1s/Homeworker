from openpyxl import Workbook

wb = Workbook("Excel.xlsx")
ws = wb.active
data = data.rows
c = 0

for value in data:
    ws.cell(1, column)
print(ws.cell)

# wb.save('Excel2.xlsx')
