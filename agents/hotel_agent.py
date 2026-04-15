from services.hotel_api import get_hotels_api

def get_hotels(data):

    destination = data.get("destination")

    return get_hotels_api(destination)