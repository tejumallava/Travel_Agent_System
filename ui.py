import gradio as gr
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")


def travel_ui(user_input):
    try:
        res = requests.post(
            f"{API_URL}/travel-text",
            json={"query": user_input},
            timeout=60
        )
        return res.json()
    except Exception as e:
        return {"error": str(e)}


demo = gr.Interface(
    fn=travel_ui,
    inputs=gr.Textbox(
        label="Enter travel request",
        placeholder="I want to go from Paris to Atlanta next week"
    ),
    outputs="json",
    title="✈️ AI Travel Agent",
    description="Enter your travel plan and get results"
)


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )