from flask import Flask, jsonify

app = Flask(__name__)

# Sample user data (can be replaced with database integration)
users = [
    {"id": 1, "username": "john_doe", "email": "john@example.com", "role": "customer"},
    {"id": 2, "username": "jane_smith", "email": "jane@example.com", "role": "admin"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
