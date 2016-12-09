import Excel
import XML
import Mail


xml = XML.get_xml() #get weather report in xml format
date, time, temp = XML.parse_xml(xml) #parse and extract xml into date, time, temp

file_name = date.isoformat() + ".xlsx" #file name = date.xlsx

#get workbook and worksheet
workbook = Excel.get_workbook(file_name)
worksheet = workbook.active

Excel.enter_data(time, temp, worksheet) #enter time, temp data into the sheet
Excel.update_chart(date, worksheet) #update the chart on the sheet

workbook.save(file_name) #save workbook

if time.hour == 23 : #sends mail at the end of day
    Mail.send("mdicrescio@csc271.adelphi.edu","Daily weather report: "+ date.isoformat(), file_name)
