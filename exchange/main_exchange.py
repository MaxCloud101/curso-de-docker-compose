from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def exchange_from_dollar():
    # This funcion convert from dollar to EURO or GBP
    currency = request.args.get('currency')
    amount = request.args.get('amount', type=float)
    response = -1

    if currency not in ['EURO', 'GBP'] or amount < 1:
        return str(response)

    if currency == 'EURO':
        response = amount * 0.86
    
    if currency == 'GBP':
        response = amount * 0.74 

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
