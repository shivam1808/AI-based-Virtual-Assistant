
import requests, json


def check_weather(city):

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = city
    API_KEY = "fb25040a8ad9a4be3e4f16d44196bc27"

    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

    response = requests.get(URL)

    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        print(f"{CITY:-^30}")
        weat = "Temperature: "+str(temperature)+"\n"+"Humidity: "+str(humidity)+"\n"+"Pressure: "+str(pressure)+"\n"+"Weather Report: "+str(report[0]['description'])
        
        return weat
    else:
        # showing the error message
        print("Error in the HTTP request")
        return "Nothing"

