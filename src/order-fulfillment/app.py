from flask import Flask, jsonify

app = Flask(__name__)

# Sample order data (can be replaced with database integration)
orders = [
    {"id": 1, "user_id": 1, "product_id": 1, "quantity": 2, "status": "pending"},
    {"id": 2, "user_id": 2, "product_id": 2, "quantity": 1, "status": "shipped"}
]

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
