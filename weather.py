import requests, json
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

def check_weather(city=None):

    if not city:
        city = get_location()['city']

    # Checks country
    country = get_location()['country_name']

    # If country is US, shows weather in Fahrenheit
    if country == 'United States':
        send_url = (
            "http://api.openweathermap.org/data/2.5/weather?q={0}"
            "&APPID=fb25040a8ad9a4be3e4f16d44196bc27&units=imperial".format(
                city)
        )
        unit = ' ºF in '

    # If country is not US, shows weather in Celsius
    else:
        send_url = (
            "http://api.openweathermap.org/data/2.5/weather?q={0}"
            "&APPID=fb25040a8ad9a4be3e4f16d44196bc27&units=metric".format(
                city)
        )
        unit = ' ºC in '
    r = requests.get(send_url)
    j = json.loads(r.text)

    # check if the city entered is not found
    if 'message' in j and j['message'] == 'city not found':
        return Fore.BLUE + "City Not Found" + Fore.RESET

    else:
        temperature = j['main']['temp']
        description = j['weather'][0]['main']
        return ("{COLOR}It's {TEMP}{UNIT}{CITY} ({DESCR}){COLOR_RESET}"
              .format(COLOR=Fore.BLUE, COLOR_RESET=Fore.RESET,
                      TEMP=temperature, UNIT=unit, CITY=city,
                      DESCR=description))

