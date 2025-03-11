Flask Web Application

Project Overview

This is a Flask web application that demonstrates user registration and database management using SQLAlchemy. The application follows best practices for file architecture, database migrations, unit testing, and Flask Blueprints.

Features

Displays a homepage with registered users.

Uses Flask Blueprints to organize routes.

Implements SQLAlchemy for database management.

Supports database migrations with Flask-Migrate.

Includes unit tests for models and routes.

Project Structure
flask-web-app/
│── application/            # Main app folder
│   ├── bp/homepage/        # Blueprint for homepage
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── database/           # Database-related files
│   │   ├── __init__.py
│   ├── models.py           # SQLAlchemy models
│── migrations/             # Flask-Migrate migration scripts
│── tests/                  # Unit tests
│   ├── test_models.py
│   ├── test_routes.py
│── config.py               # Configuration settings
│── requirements.txt        # List of dependencies
│── wsgi.py                 # Entry point for running the app
│── README.md               # Project documentation

Installation and Setup

Prerequisites

Ensure you have Python 3.12 and virtual environment support installed.

1. Clone the Repository
git clone https://github.com/EnghelRojas/flask-web-app.git
cd flask-web-app

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate

3. Install Dependencies3. Install Dependencies
pip install -r requirements.txt

4. Initialize the Database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

5. Run the Application
flask run
The app will be available at http://127.0.0.1:5000/.

Adding Users Manually
flask shell

from application.models import db, User
new_user = User(username="Charlie", email="charlie@example.com")
db.session.add(new_user)
db.session.commit()

Running Tests
pytest
GitHub Repository
Find the latest code on GitHub:
https://github.com/EnghelRojas/flask-web-app

Author

Enghel Rojas
