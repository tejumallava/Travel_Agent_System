import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_api(city):

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        if "main" not in data:
            return {
                "city": city,
                "error": data.get("message", "API error"),
                "temperature": None,
                "condition": "unknown"
            }

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }

    except Exception as e:
        return {
            "city": city,
            "error": str(e),
            "temperature": None,
            "condition": "unknown"
        }