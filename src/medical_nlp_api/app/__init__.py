from flask import Flask, jsonify
from flask_cors import CORS
from pyngrok import ngrok

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Ngrok for tunneling (optional in production)
    public_url = ngrok.connect(8000)
    print(f" * Running on {public_url}")
    

    from .routes import medical_bp
    app.register_blueprint(medical_bp)

    return app
