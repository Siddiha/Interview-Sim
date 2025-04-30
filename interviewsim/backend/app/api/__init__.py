from flask import Blueprint

api = Blueprint('api', __name__)

# Import your routes here
from . import example_routes  # Replace with actual route files as needed

def register_routes(app):
    app.register_blueprint(api, url_prefix='/api')