import gradio as gr
import requests

API_URL = "https://travelagent-production-dc43.up.railway.app/travel-text"


def get_travel_plan(query):
    try:
        response = requests.post(API_URL, json={"query": query})
        data = response.json()

        if "error" in data:
            return f"❌ Error: {data['error']}"

        parsed = data.get("parsed_request", {})
        result = data.get("result", {})

        return f"""
✈️ Travel Plan

From: {parsed.get('origin')}
To: {parsed.get('destination')}

Flights:
{result.get('flights', 'No flights found')}

Hotels:
{result.get('hotels', 'No hotels found')}
        """

    except Exception as e:
        return f"Error: {str(e)}"


with gr.Blocks() as app:
    gr.Markdown("# 🌍 AI Travel Agent")

    query = gr.Textbox(label="Enter your travel request")

    btn = gr.Button("Search")

    output = gr.Textbox()

    btn.click(fn=get_travel_plan, inputs=query, outputs=output)

app.launch()