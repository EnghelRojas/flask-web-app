from flask import Blueprint, render_template
from application.database import User  # Import User model

homepage_bp = Blueprint("homepage", __name__)

@homepage_bp.route("/")
def homepage():
    users = User.query.all()  # Fetch users from the database
    return render_template("users.html", users=users)  # Pass data to template
