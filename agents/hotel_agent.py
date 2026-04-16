from services.hotel_api import get_hotels_api

def get_hotels(city):
    return get_hotels_api(city)