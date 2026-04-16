from services.aviationstack_api import get_flights_api
from services.weather_api import get_weather_api
from services.hotel_api import get_hotels_api
from utils.normalizer import normalize_flights
from utils.helpers import safe

def run_orchestrator(parsed):

    origin = parsed.get("origin") or "Delhi"
    destination = parsed.get("destination") or "Dubai"



    if not destination:
        destination = parsed.get("origin")  # fallback 1
    if not destination:
        destination = "Paris"  # last fallback only    
    flights_raw = get_flights_api(origin, destination)
    flights = normalize_flights(flights_raw)

    hotels = get_hotels_api(destination)
    weather = get_weather_api(destination)

    return {
        "flights": flights,
        "hotels": hotels,
        "weather": weather
    }