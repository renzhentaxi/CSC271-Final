import openpyxl

def get_workbook(date):
    file_name = date.isoformat()
    if os.path.exists(file_name):
        return openpyxl.load_workbook(file_name)
    else:
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet['A1'] = "Time"
        worksheet['B1'] = "Temperature (Celsius)"
        return workbook

def enter_data(time, temp, worksheet):
def update_chart(workbook, worksheet)
