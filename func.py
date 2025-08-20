import requests
import os
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    This function takes an city name as input, then uses the Open Weather API to 
    retrieve temp in celsius, humidity, and description
    """

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }

    response = requests.get(url, params=params)

    data = response.json()

    humidity = data["main"]["humidity"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return temp, humidity, description
# print(f"City = {city}")
# print(f"Temperature = {temp}")
# print(f"Humidity = {humidity}")
# print(f"Description = {description}")