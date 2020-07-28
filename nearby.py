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

def search_near(things, city=0):
    if city:
        print("{COLOR}Hold on! I'll show {THINGS} near {CITY}{COLOR_RESET}"
              .format(COLOR=Fore.GREEN, COLOR_RESET=Fore.RESET,
                      THINGS=things, CITY=city))
    else:
        url = "https://www.google.com/maps/search/{0}/@{1},{2}".format(
            things, get_location()['latitude'], get_location()['longitude'])
    webbrowser.open(url)
    return ("{COLOR}Hold on!, I'll show {THINGS} near you{COLOR_RESET}"
              .format(COLOR=Fore.GREEN, COLOR_RESET=Fore.RESET, THINGS=things))
