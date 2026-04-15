from fastapi import FastAPI
import gradio as gr
import os

app = FastAPI()

# -------------------
# YOUR API ROUTES
# -------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------
# GRADIO UI
# -------------------
def travel_ui(text):
    return {"message": f"You entered: {text}"}


demo = gr.Interface(
    fn=travel_ui,
    inputs="text",
    outputs="json",
    title="Travel Agent UI"
)

# IMPORTANT: mount Gradio on root "/"
app = gr.mount_gradio_app(app, demo, path="/")


# -------------------
# ENTRY POINT
# -------------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)