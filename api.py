from db.aggregations import getInRange, getNearest
from bson import json_util 
import json
from mixed_mobility import calc

from flask import Flask, jsonify, request, Response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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

@app.route("/api/calc", methods=['POST'])
def calcRoute():
    req = request.get_json()
    try:
        res = calc(
            {
                'lat': float(req['from']['lat']),
                'lng': float(req['from']['lon'])
            },
            {
                'lat': float(req['to']['lat']),
                'lng': float(req['to']['lon'])
            },
            subway=False,
            reverse=bool(req['reversed'])
        )
    except Exception:
        res = calc(
            {
                'lat': float(req['from']['lat']),
                'lng': float(req['from']['lon'])
            },
            {
                'lat': float(req['to']['lat']),
                'lng': float(req['to']['lon'])
            },
            subway=True,
            reverse=bool(req['reversed'])
        )

    return Response(response=json.dumps(res),
                    status=200,
                    mimetype="application/json")

app.run(host='0.0.0.0', debug=True)