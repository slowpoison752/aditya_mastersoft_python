from basicProject import db,login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, unique = True, index=True)
    username = db.Column(db.String,unique =True, index = True)
    pwd_hash = db.Column(db.String)

    def __init__(self, email,username,password):
        self.email = email
        self.username = username
        self.pwd_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.pwd_hash,password)
