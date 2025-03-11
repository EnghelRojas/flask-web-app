import pytest
from application import create_app, db
from application.database.models import User
from datetime import datetime

# Fixture to create and destroy the app and database for each test
@pytest.fixture
def app():
    app = create_app()

    # Set up the database for testing
    with app.app_context():
        db.create_all()  # This creates all tables based on the models

    yield app

    # Clean up after tests
    with app.app_context():
        db.drop_all()  # Cleanup after tests

# Test the creation of a user
def test_create_user(app):
    with app.app_context():
        new_user = User(username="testuser", email="testuser@example.com")
        db.session.add(new_user)
        db.session.commit()

        # Verify the insertion
        user = User.query.filter_by(username="testuser").first()
        assert user is not None
        assert user.username == "testuser"
