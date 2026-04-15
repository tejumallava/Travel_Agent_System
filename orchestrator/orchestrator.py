from agents.requirement_agent import check_requirements
from agents.flight_agent import get_flights
from agents.hotel_agent import get_hotels
from agents.weather_agent import get_weather


def run_orchestrator(data):

    if not check_requirements(data):
        return {"error": "Invalid travel request"}

    flights = get_flights(data)
    hotels = get_hotels(data)
    weather = get_weather(data)

    return {
        "flights": flights,
        "hotels": hotels,
        "weather": weather
    }