from app import create_app, db
from app.models import User

app = create_app()

# Initialize the app with the database
with app.app_context():
    new_user = User(username='bfirst', email='bfirst@example.com')
    new_user.set_password('1234')
    db.session.add(new_user)
    db.session.commit()
    print("User added successfully!")
