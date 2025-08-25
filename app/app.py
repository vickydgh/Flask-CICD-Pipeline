from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Flask on EKS! Build: {os.getenv('BUILD_NUMBER', 'local')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/health")
def health():
    return "OK", 200
