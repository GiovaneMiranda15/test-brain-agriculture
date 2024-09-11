from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produtor(db.Model):
    __tablename__ = 'produtor'
    
    id = db.Column(db.Integer, primary_key=True)
    cpf_cnpj = db.Column(db.String(14), unique=True, nullable=False)
    nome_produtor = db.Column(db.String(100), nullable=False)
    nome_fazenda = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    area_total = db.Column(db.Numeric(10, 2), nullable=False)
    area_agricultavel = db.Column(db.Numeric(10, 2), nullable=False)
    area_vegetacao = db.Column(db.Numeric(10, 2), nullable=False)
    culturas = db.relationship('Cultura', backref='produtor', cascade="all, delete-orphan")