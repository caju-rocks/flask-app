import os
import time
import random

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    version = os.getenv("VERSION")
    hostname = os.getenv("HOSTNAME")
    response = {"app": f"flask-app-{version}", "hostname": f"{hostname}"}
    return response

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
