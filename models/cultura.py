from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cultura(db.Model):
    __tablename__ = 'cultura'
    
    id = db.Column(db.Integer, primary_key=True)
    produtor_id = db.Column(db.Integer, db.ForeignKey('produtor.id'), nullable=False)
    cultura = db.Column(db.String(100), nullable=False)
    area = db.Column(db.Numeric(10, 2), nullable=True)
