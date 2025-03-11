from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()  # Database instance

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Update as needed
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Bind database to app
    Migrate(app, db)  # Initialize Flask-Migrate

    from application.bp.homepage import homepage_bp
    app.register_blueprint(homepage_bp)

    return app
