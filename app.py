from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Azure Flask App"

# Health check route
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# GET route
@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Supraja"},
        {"id": 2, "name": "Naveen"}
    ]
    return jsonify(users)

# POST route
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    return jsonify({
        "message": "User added successfully",
        "user": data
    })

# Dynamic route
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)