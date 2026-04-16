def get_weather(city):
    if not city:
        return {
            "city": "unknown",
            "temperature": 28,
            "condition": "clear (fallback)"
        }

    # call API normally