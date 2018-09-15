from db.aggregations import getInRange, getNearest
from bson import json_util 

from flask import Flask, jsonify, request, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/getInRange", methods=['POST'])
def getInRangeRoute():
    req = request.get_json()
    res = getInRange(
        req['type'],
        float(req['lon']),
        float(req['lat']),
        float(req['radius'])
    )
    return Response(response=json_util.dumps(res),
                    status=200,
                    mimetype="application/json")

@app.route("/api/getNearest", methods=['POST'])
def getNearestRoute():
    req = request.get_json()
    res = getNearest(
        req['type'],
        float(req['lon']),
        float(req['lat'])
    )
    return Response(response=json_util.dumps(res),
                    status=200,
                    mimetype="application/json")

app.run(host='0.0.0.0', debug=True)