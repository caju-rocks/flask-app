import os

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    version = os.getenv("VERSION")
    hostname = os.getenv("HOSTNAME")
    response = {"app": f"flask-app-{version}", "hostname": f"{hostname}"}
    return response


@app.route("/about")
def about():
    response = {"message": "this should be about the app"}
    return response
