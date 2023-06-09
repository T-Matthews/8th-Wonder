from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from flask_login import LoginManager, UserMixin
#create the instance of our Login Manager
login = LoginManager()

#tell our login manager how it can access a User object from a user_id
@login.user_loader
def load_user(userid):
    return User.query.get(userid)


from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.String(40),primary_key=True)
    username=db.Column(db.String(100),nullable=False,unique=True)
    email=db.Column(db.String(100),nullable = False, unique = True)
    password=db.Column(db.String(255),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))

    def __init__(self,username,email,password,first_name="",last_name=""):
        self.username = username.title()
        self.email=email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)








    """
    OLD ATTRIBUTES BELOW, UPDATED ABOVE
    """
    # id = db.Column(db.Integer,primary_key=True)
    # first_name = db.Column(db.String(20),nullable=False)
    # last_name = db.Column(db.String(20),nullable=False)
    # created = db.Column(db.DateTime, default=datetime.utcnow())
    # email= db.Column(db.String(40),nullable=False)


