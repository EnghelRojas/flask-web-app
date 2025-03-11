from flask import Blueprint

homepage_bp = Blueprint('homepage', __name__)

from . import routes  # Import routes AFTER defining the Blueprint
