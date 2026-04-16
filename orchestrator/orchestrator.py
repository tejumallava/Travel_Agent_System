from services.aviationstack_api import get_flights_api
from services.weather_api import get_weather_api
from services.hotel_api import get_hotels_api
from utils.normalizer import normalize_flights

def run_orchestrator(parsed):

    origin = safe(parsed.get("origin"), "Delhi")
    destination = safe(parsed.get("destination"), "Dubai")


    if not destination:
       destination = "Dubai"  # fallback default city
    flights_raw = get_flights_api(origin, destination)
    flights = normalize_flights(flights_raw)

    hotels = get_hotels_api(destination)
    weather = get_weather_api(destination)

    return {
        "flights": flights,
        "hotels": hotels,
        "weather": weather
    }