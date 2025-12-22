from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    try:
        data = request.get_json()

        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

        cf = fetch_conversion_factor(source_currency, target_currency)
        final_amount = round(amount * cf, 2)

        return jsonify({
            "fulfillmentText": f"{amount} {source_currency} is {final_amount} {target_currency}"
        })

    except Exception as e:
        print(e)
        return jsonify({
            "fulfillmentText": "Something went wrong. Please try again."
        })

def fetch_conversion_factor(source, target):
    url = f"https://v6.exchangerate-api.com/v6/e0c3ac04b4d78492c71afb4b/latest/{source}"
    response = requests.get(url).json()
    return response["conversion_rates"][target]

if __name__ == "__main__":
    app.run()

