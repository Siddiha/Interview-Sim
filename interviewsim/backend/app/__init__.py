from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load configuration from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
    app.config['DEBUG'] = os.getenv('DEBUG', 'True') == 'True'

    # Register blueprints
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app

app = create_app()