from flask import Flask, render_template, request
import os
import time
from .model import Summarizer 

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "summary_model")

model_path = os.path.join(MODEL_DIR, "model")
tokenizer_path = os.path.join(MODEL_DIR, "tokenizer")

summarizer = None
model_loaded = False

def get_summarizer():
    global summarizer, model_loaded
    if summarizer is None:
        try:
            start_time = time.time()
            summarizer = Summarizer(
                model_path=model_path,
                tokenizer_path=tokenizer_path
            )
            model_loaded = True
            end_time = time.time()
            
        except Exception as e:
            summarizer = None
            model_loaded = False
            print(f"Error loading model: {e}")
    return summarizer


get_summarizer()

@app.route("/", methods=["GET", "POST"])
def home():
    summary_result = ""
    original_text = ""

    if request.method == "POST":
        original_text = request.form.get("text", "")
        try:
            start_time = time.time()
            if get_summarizer():
                summary_result = summarizer.summarize(original_text)
            else:
                summary_result = "⚠️ Model not loaded. Check logs."
            end_time = time.time()
            
        except Exception as e:
            summary_result = f"Error during summarization: {e}"
            

    return render_template(
        "index.html",
        summary=summary_result,
        original_text=original_text,
        model_loaded=model_loaded
    )

if __name__ == "__main__":
    app.run(debug=True)