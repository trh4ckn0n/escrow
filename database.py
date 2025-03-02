# database.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Signalement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    telephone = db.Column(db.String(20), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=False)
    date_signalement = db.Column(db.DateTime, default=db.func.current_timestamp())
