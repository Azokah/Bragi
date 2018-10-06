from flask import json, jsonify

def loadJSONfromStatic(path):
    jsonfile = json.loads(open(path).read())
    return jsonify(jsonfile)