import re

def parse_user_request(text):
    # simple MVP parser (upgrade later with LLM)
    return {
        "origin": extract_city(text, 0),
        "destination": extract_city(text, 1),
        "raw": text
    }

def extract_city(text, index):
    cities = re.findall(r"[A-Z][a-z]+", text)
    return cities[index] if len(cities) > index else None