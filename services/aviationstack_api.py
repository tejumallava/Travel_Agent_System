import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

def get_flights_api(origin=None, destination=None):

    try:
        url = "http://api.aviationstack.com/v1/flights"

        params = {
            "access_key": API_KEY,
            "limit": 5
        }

        if origin:
            params["dep_iata"] = origin
        if destination:
            params["arr_iata"] = destination

        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        return data.get("data", [])

    except Exception as e:
        return [{
            "error": str(e)
        }]