import pytest
from application import create_app, db

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()  # Ensure database tables exist
    yield app
    with app.app_context():
        db.drop_all()  # Cleanup after tests

@pytest.fixture
def client(app):
    return app.test_client()
