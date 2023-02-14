from website import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__='users'
    id= db.Column(db.Integer, primary_key=True)
    nom= db.Column(db.String(50), unique=True, nullable = False)
    prenom= db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password= db.Column(db.String(80),nullable=False)

