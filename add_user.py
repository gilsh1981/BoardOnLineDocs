from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()

    # Add users
    users = [
        {"username": "Bfirst", "email": "giladin.sh@gmail.com", "password": "1234"},
        {"username": "Gil", "email": "gilsbox2@gmail.com", "password": "1234"},
        {"username": "Yehuda", "email": "gilshmarketing@gmail.com", "password": "1234"},
        {"username": "Doron", "email": "shehtihengili@gmail.com", "password": "1234"},
    ]

    for user_data in users:
        user = User.query.filter_by(username=user_data["username"]).first()
        if user is None:
            new_user = User(username=user_data["username"], email=user_data["email"])
            new_user.set_password(user_data["password"])
            db.session.add(new_user)

    db.session.commit()

print("Users added successfully!")
