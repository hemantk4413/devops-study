from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Root endpoint that returns a welcome message"""
    return jsonify(message="Welcome to the DevOps Study App!")


@app.route('/api/users')
def get_users():
    """Get a list of sample users"""
    users = [
        {"id": 1, "name": "Alice", "role": "DevOps Engineer"},
        {"id": 2, "name": "Bob", "role": "Backend Developer"},
        {"id": 3, "name": "Charlie", "role": "DevOps Engineer"}
    ]
    return jsonify(users=users)

@app.route('/api/info')
def info():
    """Get application information"""
    return jsonify(
        app_name="DevOps Study App",
        environment="development",
        features=["user management", "health checks", "api endpoints"]
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
