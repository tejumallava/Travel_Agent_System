import requests
import os

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    if "current" not in data:
        return {"error": data}

    return {
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    }