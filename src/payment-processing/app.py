from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/payment', methods=['POST'])
def process_payment():
    data = request.json
    # Mock payment processing logic
    if 'amount' not in data or 'card_number' not in data or 'expiry' not in data:
        return jsonify({"error": "Invalid payment data"}), 400
    if data['amount'] <= 0:
        return jsonify({"error": "Invalid amount"}), 400
    # Perform payment processing (integration with payment gateway, etc.)
    return jsonify({"message": "Payment processed successfully", "amount": data['amount']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
