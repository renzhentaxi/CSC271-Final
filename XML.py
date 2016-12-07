import requests
import xml.etree.ElementTree as ET
import datetime
#: returns a string representation of the report in xml
def get_xml():
    url = "http://www.aviationweather.gov/adds/dataserver_current/httpparam"
    parameters = {
    'dataSource' : 'metars',
    'requestType' : 'retrieve',
    'format': 'xml',
    'stationString' : 'kjfk',
    'mostRecent' : True,
    'hoursBeforeNow': 1
    }
    response = requests.get(url, params = parameters)
    return response.text

def parse_xml(report):
    element = ET.fromstring(report).find('data').find('METAR')

    date, time = element.find('observation_time').text[:-1].split('T', 1)
    year, month, day = [int(i) for i in date.split("-")]
    hour, minute, second = [int(i) for i in time.split(":")]

    return (
        datetime.date(year, month, day), #date
        datetime.time(hour, minute, second), #time
        float(element.find('temp_c').text) #temp
    )
