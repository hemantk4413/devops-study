from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Root endpoint that returns a welcome message"""
<<<<<<< HEAD
    return jsonify(message="Welcome to Main Branch - DevOps App!", author="main")
=======
    return jsonify(message="Hello from conflict-test branch!", version="2.0")
>>>>>>> conflict-test

@app.route('/api/health')
 def health():
     """Health check """
     return jsonify(status="healthy", version="1.0.0")
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
