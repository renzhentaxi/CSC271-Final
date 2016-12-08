import requests


def send_file(email, file_name):
    domain="sandboxfc9548525d4a46769e02ec8adfe1f7eb.mailgun.org"
    url = "https://api.mailgun.net/v3/" + domain + "/messages"
    auth = ("api","key-6e416335a388b25ade0d655cc229a751")
    files = {"attachment": open(file_name,"rb")}
    data={
    "from": "weather_report@" + domain + "",
    "to": email,
    "subject": "Weather Report",
    "text": " "}

    return requests.post(url, auth = auth, files = files, data= data)
