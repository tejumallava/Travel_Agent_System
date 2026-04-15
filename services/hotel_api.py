import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "booking-com15.p.rapidapi.com"


def get_hotels_api(city):

    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    params = {
        "dest_name": city,
        "search_type": "CITY",
        "adults": "2",
        "room_qty": "1",
        "page_number": "1",
        "units": "metric",
        "currency_code": "USD"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        print("HOTEL API STATUS:", response.status_code)

        hotels = []

        # NEW API STRUCTURE
        for h in data.get("data", {}).get("hotels", [])[:5]:
            hotels.append({
                "name": h.get("name"),
                "price": h.get("priceBreakdown", {}).get("grossPrice", {}).get("value"),
                "rating": h.get("reviewScore")
            })

        if not hotels:
            return fallback_hotels()

        return hotels

    except Exception as e:
        print("HOTEL API ERROR:", e)
        return fallback_hotels()


def fallback_hotels():
    return [
        {"name": "Fallback Hotel A", "price": 120, "rating": 4.1},
        {"name": "Fallback Hotel B", "price": 90, "rating": 3.9}
    ]