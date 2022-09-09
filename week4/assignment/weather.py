"""Weather Program Python Project Using the requests library,
create a program that will take a city name as input and
return the current weather for that city. The program should
also save the city name and the current weather to a file.
The program should also be able to read the file and
print the city name and the current weather. Use this API to get the weather data:
https://openweathermap.org/current"""

from urllib import response
import requests #external lib
import json
import sys

apikey="12345678912345"
apiurl="http.smsm.sm"

def getweather(city):
    weather_url=f"{apiurl}?q{city}&appid={apikey}"
    response=requests.get(weather_url)
    return response.json

def print_weather(data)
