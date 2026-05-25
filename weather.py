import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        print(f"\nWeather in {name}")
        print(f"Temperature : {temp}°C")
        print(f"Condition   : {description.capitalize()}")
        print(f"Humidity    : {humidity}%")
        print(f"Wind speed  : {wind} m/s")
    else:
        print(f"Could not find weather for '{city}'. Try another city name.")

city = input("Enter city name: ")
get_weather(city)