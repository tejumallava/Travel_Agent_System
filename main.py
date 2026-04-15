from fastapi import FastAPI
import gradio as gr
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

def travel_ui(text):
    return {"message": text}

demo = gr.Interface(
    fn=travel_ui,
    inputs="text",
    outputs="json",
    title="Travel AI UI"
)

app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)