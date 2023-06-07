from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    email= db.Column(db.String(40),nullable=False)