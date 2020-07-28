import json
import webbrowser
import requests

location = 0

def get_location():
    global location
    if not location:
        #print("Getting Location ... ")
        send_url = 'http://api.ipstack.com/check?access_key=71cc794a160cbca5d796f62cee9dc128&output=json&legacy=1'
        r = requests.get(send_url)
        location = json.loads(r.text)

    if "Morādābād" == location['city']:
        return "Moradabad"
    return location['city']