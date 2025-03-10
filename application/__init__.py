from flask import Flask
from application.bp.homepage import homepage_bp  # Import homepage blueprint
from application.database import db  # Import SQLAlchemy database instance

def create_app():
    app = Flask(__name__)

    # Configuration settings (you can modify config.py later)
    app.config.from_object("config")

    # Initialize database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(homepage_bp)

    return app
