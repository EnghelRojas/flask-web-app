from flask import render_template
from application.database.models import User  # Import User model
from application.bp.homepage import homepage_bp
from application import db

@homepage_bp.route("/")
def homepage():
    users = User.query.all()  # Fetch all users from the database
    return render_template("index.html", users=users)
