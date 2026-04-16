def normalize_flights(flights):
    cleaned = []

    for f in flights:
        if "error" in f:
            continue

        cleaned.append({
            "airline": f.get("airline", {}).get("name"),
            "departure": f.get("departure", {}).get("airport"),
            "arrival": f.get("arrival", {}).get("airport"),
            "time": f.get("departure", {}).get("scheduled")
        })

    return cleaned
