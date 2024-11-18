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
{"timestamp": "2024-11-18 16:35:52,853", "endpoint": "[31m[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.[0m
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.0.2:5000", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:35:52,853", "endpoint": "[33mPress CTRL+C to quit[0m", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:36:26,102", "endpoint": "/data", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:36:26,103", "endpoint": "192.168.65.1 - - [18/Nov/2024 16:36:26] "GET /data HTTP/1.1" 200 -", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:36:58,879", "endpoint": "/", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:36:58,880", "endpoint": "192.168.65.1 - - [18/Nov/2024 16:36:58] "GET / HTTP/1.1" 200 -", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:37:10,791", "endpoint": "/data", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:37:10,792", "endpoint": "192.168.65.1 - - [18/Nov/2024 16:37:10] "GET /data HTTP/1.1" 200 -", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:38:22,320", "endpoint": "/data", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:38:22,322", "endpoint": "192.168.65.1 - - [18/Nov/2024 16:38:22] "GET /data HTTP/1.1" 200 -", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:38:26,688", "endpoint": "/", "status_code": "INFO"}
{"timestamp": "2024-11-18 16:38:26,690", "endpoint": "192.168.65.1 - - [18/Nov/2024 16:38:26] "GET / HTTP/1.1" 200 -", "status_code": "INFO"}
