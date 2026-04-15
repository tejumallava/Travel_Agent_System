import requests
import os

def get_weather_api(city):
    API_KEY = os.getenv("WEATHER_API_KEY")  # make sure Railway uses same name

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        # safety check
        if res.status_code != 200:
            return {
                "error": data.get("message", "Weather API failed"),
                "temperature": None,
                "condition": None
            }

        return {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }

    except Exception as e:
        return {
            "error": str(e),
            "temperature": None,
            "condition": None
        }