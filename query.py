from application import create_app, db
from application.database.models import User
from datetime import datetime

app = create_app()
with app.app_context():
    db.create_all()  # Ensure tables exist

    if not User.query.first():  # Check if database is empty
        user1 = User(username="Alice", email="alice@example.com", date_added=datetime.utcnow())
        user2 = User(username="Bob", email="bob@example.com", date_added=datetime.utcnow())

        db.session.add_all([user1, user2])
        db.session.commit()
        print("✅ Users added successfully!")
    else:
        print("✅ Users already exist.")
