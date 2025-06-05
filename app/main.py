from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "👋 Welcome to the Uptime Checker API"

@app.route("/check")
def check_website():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    if not url.startswith("http"):
        url = "http://" + url

    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()

        return jsonify({
            "url": url,
            "status": "Online" if response.status_code == 200 else "Unstable",
            "status_code": response.status_code,
            "response_time_ms": int((end - start) * 1000)
        })

    except requests.exceptions.RequestException:
        return jsonify({
            "url": url,
            "status": "Offline"
        })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
