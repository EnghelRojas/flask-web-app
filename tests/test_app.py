import pytest
from application import create_app, db

@pytest.fixture
def app():
    app = create_app()

    # Ensure database is clean before testing
    with app.app_context():
        db.drop_all()  # Drop existing tables
        db.create_all()  # Create new tables for tests

    yield app

    with app.app_context():
        db.drop_all()  # Cleanup after tests

@pytest.fixture
def client(app):
    return app.test_client()
