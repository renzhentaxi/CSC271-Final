The System first retrieves the string(containing the weather report in XML format) using the requests module and the aviation weather API.
Then the string is parsed using methods from xml.etree.ElementTree and the data are extracted from it into a dictionary object.
The data extracted contains three entries

    temp: the temperature in Celsius. Type = float
    time: the time when the temperature was recorded. Type = datetime.time
    day: the day when the temperature was recorded. Type = datetime.date

If there were an excel file with the name of the date when the temperature was recorded, the data would be entered into that file.
If there is no such excel file, an Excel file with the name of the date is created.
The loading,manipulating, saving of the Excel files is handled with methods from the openpyxl module.

Each excel file contains one spreadsheet.
The sheet contains two columns of data formatted using the following format:

| Time  | Temperature (Celsius)|
| ----- | --------------------|
| 12:10 | 10.2 |
| 13:10 | 13.1 |
| 14:10 | 12.3 |
| 15:10 | 15.2 |


It also contains a Scatter Chart.
The chart's x-axis is time and y-axis is temperature.
The title of the chart is the date when the report is created.