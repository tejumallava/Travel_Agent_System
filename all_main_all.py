from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# =====================
# CONFIG (ENV VARIABLES)
# =====================
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


# =====================
# SCHEMA
# =====================
class TravelRequest(BaseModel):
    origin: str = None
    destination: str = None
    date: str = None
    travelers: int = 1
    budget: float = None


# =====================
# AGENTS
# =====================

# Requirement Agent
def check_requirements(data):
    missing = []

    if not data.origin:
        missing.append("origin")
    if not data.destination:
        missing.append("destination")
    if not data.date:
        missing.append("date")

    return missing


# Planning Agent
def create_plan():
    return ["flight", "hotel", "weather"]


# Flight Agent (Aviationstack)
def get_flights(origin, destination):
    try:
        url = "http://api.aviationstack.com/v1/flights"

        params = {
            "access_key": AVIATIONSTACK_API_KEY,
            "dep_iata": origin,
            "arr_iata": destination
        }

        response = requests.get(url, params=params)
        data = response.json()

        flights = []

        for i, f in enumerate(data.get("data", [])[:3]):
            flights.append({
                "airline": f["airline"]["name"],
                "flight": f["flight"]["iata"],
                "price": 300 + i * 50  # mock pricing
            })

        if not flights:
            raise Exception("No flights found")

        return flights

    except:
        return [
            {"airline": "Delta", "flight": "DL123", "price": 400},
            {"airline": "United", "flight": "UA456", "price": 450}
        ]


# Hotel Agent (Mock - reliable)
def get_hotels():
    return [
        {"name": "Hotel A", "price": 120},
        {"name": "Hotel B", "price": 90}
    ]


# Weather Agent
def get_weather(city):
    try:
        url = "http://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        data = response.json()

        return {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }

    except:
        return {"temperature": "25°C", "condition": "Sunny"}


# =====================
# ORCHESTRATOR
# =====================
def run_orchestrator(data):

    missing = check_requirements(data)

    if missing:
        return {"status": "missing_fields", "fields": missing}

    plan = create_plan()

    result = {}

    if "flight" in plan:
        result["flights"] = get_flights(data.origin, data.destination)

    if "hotel" in plan:
        result["hotels"] = get_hotels()

    if "weather" in plan:
        result["weather"] = get_weather(data.destination)

    return result


# =====================
# API ROUTE
# =====================
@app.post("/travel")
def travel(req: TravelRequest):
    return run_orchestrator(req)


@app.get("/")
def home():
    return {"message": "Travel AI is running 🚀"}