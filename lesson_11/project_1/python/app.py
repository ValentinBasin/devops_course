from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Set up JSON logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "endpoint": "%(message)s", "status_code": "%(levelname)s"}',
)


@app.route("/")
def home():
    logging.info("/")
    return "Welcome to the Flask App!"


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    logging.info("/submit")
    return jsonify({"message": "Data submitted successfully!", "data": data})


@app.route("/data", methods=["GET"])
def data():
    logging.info("/data")
    return jsonify({"data": "Sample data from Flask app"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
