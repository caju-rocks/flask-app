import os

from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route("/")
def index():
    version = os.getenv('VERSION')
    hostname = os.getenv('HOSTNAME')
    response = {
        "app": f"hello-flask-app-{version}",
        "hostname": f"{hostname}"
    }
    return response

@app.route("/about")
def about():
    return "about"


with app.test_request_context():
    print(url_for('index'))
