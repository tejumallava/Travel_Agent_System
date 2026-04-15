import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_user_request(query: str):
    """
    LLM-based travel parser (robust & production-ready)
    """

    if not query:
        return {}

    prompt = f"""
You are a travel intent parser.

Extract structured travel information from the user query.

Return ONLY valid JSON in this format:

{{
  "origin": "...",
  "destination": "...",
  "date": "..."
}}

Rules:
- origin: departure city (if missing, null)
- destination: arrival city (if missing, null)
- date: travel time expression (if missing, null)
- Do NOT include explanations
- Do NOT include extra text
- Output ONLY JSON

User query:
{query}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a strict JSON generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        content = response.choices[0].message.content

        # safe JSON parse
        parsed = json.loads(content)

        return parsed

    except Exception as e:
        return {
            "origin": None,
            "destination": None,
            "date": None,
            "error": str(e)
        }