from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data (can be replaced with database integration)
products = [
    {"id": 1, "name": "Bottled Water - 500ml", "price": 1.99, "description": "Pure spring water in a convenient 500ml bottle"},
    {"id": 2, "name": "Mineral Water - 1L", "price": 2.99, "description": "Naturally sourced mineral water in a 1-liter bottle"}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
