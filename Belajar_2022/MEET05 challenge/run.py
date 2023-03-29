from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>ok.</h1>"


#API GATEWAY
@app.route("/data/2.5/weather?lat=10.99&lon=44.34&appid=b6907d289e10d714a6e88b30761fae22")
def api_currency_latest():
    try:
        with open("data.json") as file:
            data = json.load(file)
    except:
        return jsonify({
            "status" : False
        })
    else:
        return jsonify(data)

app.run(debug=True)
