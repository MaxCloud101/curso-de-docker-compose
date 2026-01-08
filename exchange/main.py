from flask import Flask, request
import requests
import os

app = Flask(__name__)

EXCHANGE_URL = os.environ.get('EXCHANGE_URL')

@app.route("/to_euros")
def to_euros():
    exchange_comision = 1 # comision to exchange to euros
    amount = request.args.get('amount')
    r = requests.get("http://" + EXCHANGE_URL + "/?currency=EURO&amount=" + amount)
    return str(float(r.text) + exchange_comision)

@app.route("/to_gbp")
def to_gbp():
    exchange_comision = 2 # comision to exchange to pounds
    amount = request.args.get('amount')
    r = requests.get("http://" + EXCHANGE_URL + "/?currency=GBP&amount="+ amount)
    return str(float(r.text) + exchange_comision)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
