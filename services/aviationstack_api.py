import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

def get_flights(origin, destination):
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "dep_iata": origin,
        "arr_iata": destination,
        "limit": 5
    }

    res = requests.get(url, params=params)
    return res.json()