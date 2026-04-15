def parse_user_request(query: str):
    query = query.lower()

    patterns = [
        r'from (.*?) to (.*?)(?: on| next|$)',
        r'(.*?) to (.*?)(?: on| next|$)'
    ]

    for pattern in patterns:
        match = re.search(pattern, query)
        if match:
            return {
                "origin": match.group(1).strip().title(),
                "destination": match.group(2).strip().title(),
                "raw": query
            }

    return {
        "origin": None,
        "destination": None,
        "raw": query
    }