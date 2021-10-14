#!/usr/bin/env python3

import flask
import requests
import json
import os

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return flask.render_template("app.html")


@app.route('/predict', methods=['POST'])
def predict() -> str:
    SERVICE_HEADER = {"Host": os.environ['SERVICE_HEADER']}
    TRITON_URL = os.environ['TRITON_URL']
    question = str(flask.request.data)
    req: requests.Response = requests.post(
        url=TRITON_URL,
        json={'instances': [question]},
        headers=SERVICE_HEADER)
    print(question)
    print(req.json())
    return req.json()['predictions']


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True)
