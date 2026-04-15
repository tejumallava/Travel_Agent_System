def check_requirements(data):

    if not data.get("origin"):
        return False

    if not data.get("destination"):
        return False

    return True