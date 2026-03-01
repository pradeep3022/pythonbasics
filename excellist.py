from openpyxl import Workbook
from main import dev
wb=Workbook()
ws=wb.active

print(dev)
for i in range(len(dev)):
    ws.cell(row=i+1, column=1).value=dev[i]
wb.save("devices.xlsx")

print("Excel file created successfully.")