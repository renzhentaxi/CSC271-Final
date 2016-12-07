import openpyxl
from openpyxl.chart import ScatterChart, Reference, Series
import os
def get_workbook(file_name):
    if os.path.exists(file_name):
        return openpyxl.load_workbook(file_name)
    else:
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet['A1'] = "Time"
        worksheet['B1'] = "Temperature (Celsius)"
        return workbook

def enter_data(time, temp, worksheet):
    max_row = worksheet.max_row
    if worksheet.cell(row = max_row, column = 1).value != time: #only enter data if its different from last entr
        worksheet.cell(row = max_row + 1, column = 1).value = time
        worksheet.cell(row = max_row + 1, column = 2).value = temp

def update_chart(date, worksheet):
    chart = ScatterChart()
    chart.title = date.isoformat()
    chart.x_axis.title = worksheet["A1"].value
    chart.y_axis.title = worksheet["B1"].value
    chart.legend = None

    max_row = worksheet.max_row
    x_values = Reference(worksheet, min_col = 1, min_row = 2, max_col = 1, max_row = max_row)
    y_values = Reference(worksheet, min_col = 2, min_row = 2, max_col = 2, max_row = max_row)
    series = Series(y_values, x_values)
    chart.series.append(series)

    worksheet.add_chart(chart, "F1")
