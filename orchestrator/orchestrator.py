from agents.flight_agent import get_flights
from agents.hotel_agent import get_hotels
from agents.weather_agent import get_weather

def run_orchestrator(parsed):

    origin = parsed["origin"]
    destination = parsed["destination"]

    flights = get_flights(origin, destination)
    hotels = get_hotels(destination)
    weather = get_weather(destination)

    return {
        "flights": flights,
        "hotels": hotels,
        "weather": weather
    }