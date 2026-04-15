def get_weather(data):

    destination = data.get("destination")
    date = data.get("date")

    return {
        "temperature": 25,
        "condition": "Sunny",
        "location": destination
    }