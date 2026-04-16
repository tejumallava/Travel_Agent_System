import re

def parse_user_request(text):

    # pattern: "from X to Y"
    match = re.search(r"from (.+?) to (.+)", text, re.IGNORECASE)

    if match:
        origin = match.group(1).strip()
        destination = match.group(2).strip()
    else:
        origin = None
        destination = None

    return {
        "origin": origin,
        "destination": destination,
        "raw": text
    }