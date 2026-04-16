import requests
import os

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

CITY_TO_IATA = {
    "paris": "CDG",
    "london": "LHR",
    "dubai": "DXB",
    "delhi": "DEL",
    "new york": "JFK",
    "mumbai": "BOM"
}

def get_flights_api(origin=None, destination=None):

    try:
        origin_iata = CITY_TO_IATA.get(origin.lower()) if origin else None
        destination_iata = CITY_TO_IATA.get(destination.lower()) if destination else None

        url = "http://api.aviationstack.com/v1/flights"

        params = {
            "access_key": API_KEY,
            "limit": 5
        }

        if origin_iata:
            params["dep_iata"] = origin_iata

        if destination_iata:
            params["arr_iata"] = destination_iata

        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        return data.get("data", [])

    except Exception as e:
        return [{
            "error": str(e)
        }]