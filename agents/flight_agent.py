from services.aviationstack_api import get_flights_api

def get_flights(origin, destination):
    return get_flights_api(origin, destination)