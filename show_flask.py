from flask import Flask, request, jsonify

app = Flask(__name__)


# The problem is the data has to be extracted
# Too many check for any request
# Flask -> Gunicorn
# FastAPI -> Uvicorn
@app.post("/login")
def login():
    data = request.get_json()

    phone = data.get("phone")
    code = data.get("code")

    if not phone or not code:
        return jsonify({"error": "missing fields"}), 400

    return jsonify({"status": "ok", "phone": phone})