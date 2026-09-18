from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Backend!"

@app.route("/api")
def api():
    return {"message": "Python Backend is working"}

app.run(host="0.0.0.0", port=8000)
