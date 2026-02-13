import os
import json
from flask import Flask, jsonify, render_template

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
def home():
    dash = load_dashboard()
    return render_template("index.html", dash=dash)

@app.get("/api/dashboard")
def api_dashboard():
    return jsonify(load_dashboard())

if __name__ == "__main__":
    # 컨테이너/리버스프록시 환경에서는 반드시 0.0.0.0 로 바인딩
    app.run(host="0.0.0.0", port=5000, debug=False)
