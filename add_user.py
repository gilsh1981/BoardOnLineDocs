from app import create_app, db
from app.models import User

app = create_app()
app.app_context().push()

db.create_all()

new_user = User(username='Bfirst', email='example@example.com', phone='1234567890')
new_user.set_password('1234')
db.session.add(new_user)
db.session.commit()

print('User added successfully.')
