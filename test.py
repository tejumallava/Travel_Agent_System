import requests
import os
print("KEY:", os.getenv("OPENAI_API_KEY"))
url = "http://127.0.0.1:5000/chat"

data = {
    "message": "I want to go to Paris next month for a week after second sunday"
}

response = requests.post(url, json=data)

print(response.json())