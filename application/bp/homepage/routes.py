from flask import render_template
from application.database.models import User
from . import homepage_bp  # Import Blueprint from __init__.py

@homepage_bp.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)
