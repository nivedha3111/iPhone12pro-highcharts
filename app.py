from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 3500

@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")

@app.route("/data", methods=["GET"])
def read_json():

    coun_list = ['France','UK', 'US', 'India', 'Japan', 'Germany', 'China', 'Russia']

    rate_list = [1361, 1290, 1071, 1636, 1114, 1314, 1262, 1296]



    result_dict = {
        'coun_data': coun_list,
        
        'coun_names': 'countries',
        'title': 'iPhone 12 pro price in different countries',
        'subtitle': 'Source: https://www.statista.com/chart/19336/the-price-of-the-iphone-around-the-world/',
        'rate_data': rate_list
    }


    return jsonify(result_dict)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
