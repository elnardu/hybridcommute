from db.aggregations import getInRange, getNearest
from bson import json_util 
import json
from mixed_mobility import calc

from flask import Flask, jsonify, request, Response
from flask_cors import CORS
app = Flask(__name__, static_folder="./client/dist/", static_url_path="")
CORS(app)

@app.route("/")
def index():
    return app.send_file("./client/dist/index.html")

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
    print(req)
    try:
        res = calc(
            {
                'lat': float(req['to']['lat']),
                'lng': float(req['to']['lon'])
            },
            {
                'lat': float(req['from']['lat']),
                'lng': float(req['from']['lon'])
            },
            subway=False,
            reverse=req['reversed']
        )
    except Exception:
        res = calc(
            {
                'lat': float(req['to']['lat']),
                'lng': float(req['to']['lon'])
            },
            {
                'lat': float(req['from']['lat']),
                'lng': float(req['from']['lon'])
            },
            subway=True,
            reverse=req['reversed']
        )

    return Response(response=json.dumps(res),
                    status=200,
                    mimetype="application/json")

app.run(host='0.0.0.0', debug=True)