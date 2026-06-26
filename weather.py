import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city="Grater Noida"):
    """
    Gets current weather for a city
    Default is Delhi — user can change it
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        weather_info = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }
        
        return weather_info
    
    except Exception as e:
        return {
            "city": city,
            "temperature": "N/A",
            "humidity": "N/A", 
            "condition": "Unable to fetch weather",
            "wind_speed": "N/A"
        }