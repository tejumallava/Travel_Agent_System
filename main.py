from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="Travel Agent API 🚀")


# ---------------------------
# REQUEST MODEL
# ---------------------------
class TravelQuery(BaseModel):
    query: str


# ---------------------------
# HEALTH CHECK
# ---------------------------
@app.get("/")
def home():
    return {
        "status": "Travel Agent Running 🚀",
        "docs": "/docs"
    }


# ---------------------------
# SAFE IMPORTS (lazy loading)
# ---------------------------
def get_parser():
    try:
        from agents.parser_agent import parse_user_request
        return parse_user_request
    except Exception as e:
        raise RuntimeError(f"Parser import failed: {str(e)}")


def get_orchestrator():
    try:
        from orchestrator.orchestrator import run_orchestrator
        return run_orchestrator
    except Exception as e:
        raise RuntimeError(f"Orchestrator import failed: {str(e)}")


# ---------------------------
# MAIN ENDPOINT
# ---------------------------
@app.post("/travel-text")
def travel_text(request: TravelQuery):

    try:
        # load functions
        parse_user_request = get_parser()
        run_orchestrator = get_orchestrator()

        # 1. parse input
        parsed = parse_user_request(request.query)

        print("DEBUG INPUT:", request.query)
        print("DEBUG PARSED:", parsed)

        # 2. validation
        if not parsed:
            return {
                "error": "Parser returned None/empty",
                "input": request.query
            }

        if not parsed.get("origin") or not parsed.get("destination"):
            return {
                "error": "Missing origin or destination",
                "parsed": parsed,
                "hint": "Fix parser_agent.py output format"
            }

        # 3. orchestrator execution
        result = run_orchestrator(parsed)

        return {
            "parsed_request": parsed,
            "result": result
        }

    except Exception as e:
        return {
            "error": str(e),
            "input": request.query
        }


# ---------------------------
# RAILWAY ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )