from services.weather_api import get_weather_api

def get_weather(city):
    return get_weather_api(city)