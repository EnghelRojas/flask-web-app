from application import create_app
from application.database import db, User

app = create_app()

with app.app_context():
    db.create_all()  # Create tables

    # Sample users
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@example.com")

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    print("Database populated!")
