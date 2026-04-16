import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")
HOST = os.getenv("RAPIDAPI_HOST")

def get_hotels(city):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": HOST
    }

    params = {
        "city_name": city,
        "checkin_date": "2026-04-20",
        "checkout_date": "2026-04-21",
        "adults_number": 1
    }

    res = requests.get(url, headers=headers, params=params)
    return res.json()