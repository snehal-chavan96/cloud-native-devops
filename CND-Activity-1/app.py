
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud-Native Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background: #f0f4f8;
            }
            .card {
                background: white;
                padding: 35px;
                margin: auto;
                max-width: 550px;
                border-radius: 12px;
                box-shadow: 0 4px 12px #ccc;
            }
            h1 { color: #1769aa; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Cloud-Native Application</h1>
            <h2>Successfully Deployed!</h2>
            <p>Built with Python and Flask.</p>
            <p>Containerized using Docker.</p>
            <p>Orchestrated using Kubernetes.</p>
            <p>Container Host: """ + socket.gethostname() + """</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "cloud-native-python-app"
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
