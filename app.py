import os
import json
from flask import Flask, jsonify, render_template, redirect

app = Flask(__name__)

def load_dashboard():
    data_dir = os.getenv("DASH_DATA_DIR", "/app/data")
    path = os.path.join(data_dir, "dashboard.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return {
            "status": "MISSING",
            "error": str(e),
            "hint": f"dashboard.json not found at {path}"
        }

@app.get("/")
@app.get("/")
def home():
    return redirect("/dashboard")

@app.get("/dashboard")
def dashboard():
    dash = load_dashboard()
    return render_template("dashboard.html", dash=dash)

@app.get("/api/dashboard")
def api_dashboard():
    return jsonify(load_dashboard())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
