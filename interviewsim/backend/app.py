from flask import Flask
from flask_cors import CORS
from app.api import api_bp  # Assuming you will define your API blueprint in app/api/__init__.py

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_SETTINGS', silent=True)  # Load configuration from .env or environment variables
    CORS(app)  # Enable CORS for all routes

    # Register blueprints
    app.register_blueprint(api_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run the app on port 5000 in debug mode