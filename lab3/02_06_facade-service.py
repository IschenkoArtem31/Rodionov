from flask import Flask, request, abort, jsonify
import requests
import uuid
import random

app = Flask(__name__)

logging_service_ports = [5001, 5002, 5003] 
def get_logging_service_url():
    port = random.choice(logging_service_ports)
    return f"http://127.0.0.1:{port}/logging"

@app.route("/", methods=["POST", "GET"])
def handle_request():
    if request.method == "POST":
        _msg = request.form.get("msg")
        if not _msg:
            return "Msg error", 400
        _id = str(uuid.uuid4())
        data = {"id": _id, "msg": _msg}
        logging_service_url = get_logging_service_url()
        try:
            response = requests.post(logging_service_url, data=data)
            response.raise_for_status()  
        except requests.exceptions.RequestException as e:
            return f"Logging error: {e}", 500
        return jsonify({"id": _id, "msg": _msg}), 200
    elif request.method == "GET":
        logging_service_url = get_logging_service_url()
        try:
            log_response = requests.get(logging_service_url)
            log_response.raise_for_status()  
            log_data = log_response.json()  
            return jsonify(log_data), 200
        except requests.exceptions.RequestException as e:
            return f"Error while recieving logging data: {e}", 500
    else:
        abort(400)

if __name__ == "__main__":
    app.run(port=5000)

