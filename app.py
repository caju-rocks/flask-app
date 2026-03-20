import os
<<<<<<< HEAD
import json
from flask import Flask, make_response, request, jsonify
=======
import time
import random

from flask import Flask, url_for
>>>>>>> 19f4e4527a73e1f47257cbb48e75137599e4e3c2

app = Flask(__name__)


@app.after_request
def capture_response_headers(response):
    print("Response headers:", response.headers)
    return response


@app.route("/")
def index():
    resp = make_response(jsonify(message="hello"))

<<<<<<< HEAD
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
=======
<<<<<<< HEAD
@app.route("/v1/generate/")
def generate():
    wait = random.randint(0, 100) / 10
    response = {
        "wait-before-return": wait
    }
    time.sleep(wait)
    return response

@app.route("/about")
def about():
    response = {
        "message": "this should be about the app"
    }
=======

@app.route("/about")
def about():
    response = {"message": "this should be about the app"}
>>>>>>> d4c6dafafe3f6ed2608c52ea1c3d4572014949a0
    return response
>>>>>>> 19f4e4527a73e1f47257cbb48e75137599e4e3c2
