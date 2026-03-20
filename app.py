import os
import json
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)


@app.after_request
def capture_response_headers(response):
    print("Response headers:", response.headers)
    return response


@app.route("/")
def index():
    resp = make_response(jsonify(message="hello"))

    if request.headers.get("X-Amzn-Trace-Id"):
        resp.headers["X-Bluecharm-LB"] = "ALB"
    else:
        resp.headers["X-Bluecharm-LB"] = "CLB"
    resp.headers["X-Bluecharm-Test"] = "this is a custom header"

    response_headers = {k: v for k, v in resp.headers.items()}
    request_headers = {k: v for k, v in request.headers.items()}

    new_body = {
        "original": {"message": "debug message"},
        "response_headers": response_headers,
        "request_headers": request_headers,
    }

    resp.set_data(json.dumps(new_body))
    return resp
