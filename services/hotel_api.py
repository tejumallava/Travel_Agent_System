def get_hotels_api(city):

    # 🚨 fallback system (production pattern)
    return [
        {
            "name": f"{city} Grand Hotel",
            "price": 120,
            "rating": 4.5
        },
        {
            "name": f"{city} City Stay",
            "price": 90,
            "rating": 4.1
        },
        {
            "name": f"{city} Budget Inn",
            "price": 60,
            "rating": 3.8
        }
    ]