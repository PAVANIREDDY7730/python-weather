from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

appid = os.getenv("API_KEY")

def get_weather_data(city = "New York"):
    
    requests_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=imperial"

    weather_data = requests.get(requests_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n ***Get Current Weather Data*** \n')

    city = input("Enter city name: ")

    #check for empty string or whitespace
    if not bool(city.strip()):
        city = "New York"

    weather_data = get_weather_data(city)

    print("\n")

    pprint(weather_data)