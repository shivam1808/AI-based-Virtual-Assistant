import json
import webbrowser
import requests
from colorama import Fore

location = 0


def get_location():
    global location
    if not location:
        print("Getting Location ... ")
        send_url = 'http://api.ipstack.com/check?access_key=71cc794a160cbca5d796f62cee9dc128&output=json&legacy=1'
        r = requests.get(send_url)
        location = json.loads(r.text)
    return location


def directions(to_city, from_city=0):
    if not from_city:
        from_city = get_location()['city']
    url = "https://www.google.com/maps/dir/{0}/{1}".format(from_city, to_city)
    webbrowser.open(url)
    return "Opened in browser"