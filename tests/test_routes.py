import pytest
from application import create_app, db
from application.database.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Temporary database
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_users_display(client):
    # Add test users
    with client.application.app_context():
        user1 = User(username="Alice", email="alice@example.com")
        user2 = User(username="Bob", email="bob@example.com")
        db.session.add_all([user1, user2])
        db.session.commit()

    # Check if homepage shows users
    response = client.get("/")
    assert b"Alice" in response.data
    assert b"Bob" in response.data
