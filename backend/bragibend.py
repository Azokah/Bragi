from flask import Flask, jsonify
import json

networksMock = [
        "network":"Facebook",
        "network":"Twitter",
        "network":"Discord",
        "network":"Telegram",
        "network":"Slack"
]

app = Flask(__name__)

@app.route('/')
def helloWorld():
    hello = "Hail, Æsir!," +
            "Hail, Asyniur!" +
            " And ye, all-holy gods!" +
            "all, save that one man," +
            "who sits within there," +
            "Bragi, on yonder bench."
    return hello

@app.route('/networks')
def getNetworks():
    return networksMock