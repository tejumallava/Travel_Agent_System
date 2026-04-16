import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_api(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    res = requests.get(url, params=params)
    data = res.json()

    # 🔥 SAFE CHECK (important)
    if "main" not in data:
        return {
            "city": city,
            "error": data,
            "temperature": None,
            "condition": "unknown"
        }

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }