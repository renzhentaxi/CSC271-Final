import requests
import xml.etree.ElementTree as ET
import datetime
# retrieves the xml containing the latest weather data
# returns a string representation of the report in xml
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

# parses the xml string
# report: the xml string to be parsed
#returns a tuple in this format (date, time, temp)
def parse_xml(report):
    element = ET.fromstring(report).find('data').find('METAR')

    date, time = element.find('observation_time').text[:-1].split('T', 1)
    year, month, day = [int(i) for i in date.split("-")]
    hour, minute, second = [int(i) for i in time.split(":")]

    #translates utc time to local time 
    utc_datetime = datetime.datetime(year, month, day, hour, minute, second)
    local_datetime = utc_datetime - datetime.timedelta(hours = 5)

    return (
        local_datetime.date(), #date
        local_datetime.time(), #time
        float(element.find('temp_c').text) #temp
    )
