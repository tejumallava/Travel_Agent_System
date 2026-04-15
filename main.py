from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()


# ---------------------------
# REQUEST MODEL
# ---------------------------
class TravelQuery(BaseModel):
    query: str


# ---------------------------
# HEALTH CHECK (IMPORTANT)
# ---------------------------
@app.get("/")
def home():
    return {"status": "Travel Agent Running 🚀"}


# ---------------------------
# SAFE LAZY IMPORT WRAPPER
# ---------------------------
def get_parser():
    from agents.parser_agent import parse_user_request
    return parse_user_request


def get_orchestrator():
    from orchestrator.orchestrator import run_orchestrator
    return run_orchestrator


# ---------------------------
# MAIN ENDPOINT
# ---------------------------
@app.post("/travel-text")
def travel_text(request: TravelQuery):

    try:
        parse_user_request = get_parser()
        run_orchestrator = get_orchestrator()

        # 1. parse request
        parsed = parse_user_request(request.query)

        # 2. validation
        if not parsed.get("origin") or not parsed.get("destination"):
            return {
                "error": "Missing origin or destination",
                "parsed": parsed
            }

        # 3. run orchestrator
        result = run_orchestrator(parsed)

        return {
            "parsed_request": parsed,
            "result": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# ---------------------------
# RAILWAY ENTRY POINT (IMPORTANT)
# ---------------------------
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port
    )