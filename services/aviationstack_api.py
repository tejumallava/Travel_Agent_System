import requests
import os

AVIATION_API_KEY = os.getenv("AVIATION_API_KEY")

def get_flights_api(origin, destination):

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": AVIATION_API_KEY,
        "dep_iata": origin,
        "arr_iata": destination
    }

    response = requests.get(url, params=params)
    data = response.json()

    flights = []

    for f in data.get("data", [])[:5]:
        flights.append({
            "airline": f.get("airline", {}).get("name"),
            "flight": f.get("flight", {}).get("iata"),
            "price": 300  # API doesn't always give price
        })

    return flights