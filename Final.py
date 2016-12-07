import requests


def get_report():
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

print(get_report())
