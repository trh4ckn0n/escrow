from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Signalement(db.Model):
    __tablename__ = 'signalement'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telephone = db.Column(db.String(20))
    description = db.Column(db.Text)
    date_signalement = db.Column(db.DateTime)
