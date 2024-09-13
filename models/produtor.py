from flask_sqlalchemy import SQLAlchemy
from utils.format import formatar_cpf_cnpj, formatar_string

# Instância do SQLAlchemy
db = SQLAlchemy()

class Produtor(db.Model):
    """Modelo para a tabela `produtor`."""
    __tablename__ = 'produtor'
    
    # Definição das colunas da tabela
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

    def to_dict(self):
        """
        Converte o objeto `Produtor` para um dicionário, formatando strings e CPF/CNPJ.
        """
        return {
            "id": self.id,
            "cpf_cnpj": formatar_cpf_cnpj(self.cpf_cnpj),
            "nome_produtor": formatar_string(self.nome_produtor),
            "nome_fazenda": formatar_string(self.nome_fazenda),
            "cidade": formatar_string(self.cidade),
            "estado": formatar_string(self.estado),
            "area_total": float(self.area_total),
            "area_agricultavel": float(self.area_agricultavel),
            "area_vegetacao": float(self.area_vegetacao),
            "culturas": [cultura.to_dict() for cultura in self.culturas]
        }

    def set_data(self, data):
        """
        Atualiza o objeto `Produtor` com os dados fornecidos, formatando strings e CPF/CNPJ.
        
        Args:
            data (dict): Dados para atualizar o produtor.
        """
        self.cpf_cnpj = formatar_cpf_cnpj(data['cpf_cnpj'])
        self.nome_produtor = formatar_string(data['nome_produtor'])
        self.nome_fazenda = formatar_string(data['nome_fazenda'])
        self.cidade = formatar_string(data['cidade'])
        self.estado = formatar_string(data['estado'])
        self.area_total = data['area_total']
        self.area_agricultavel = data['area_agricultavel']
        self.area_vegetacao = data['area_vegetacao']

class Cultura(db.Model):
    """Modelo para a tabela `cultura`."""
    __tablename__ = 'cultura'
    
    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    produtor_id = db.Column(db.Integer, db.ForeignKey('produtor.id'), nullable=False)
    cultura = db.Column(db.String(100), nullable=False)
    area = db.Column(db.Numeric(10, 2), nullable=False)
    
    def to_dict(self):
        """
        Converte o objeto `Cultura` para um dicionário, formatando a string da cultura.
        """
        return {
            "id": self.id,
            "produtor_id": self.produtor_id,
            "cultura": formatar_string(self.cultura),
            "area": float(self.area)
        }
    
    def set_data(self, data):
        """
        Atualiza o objeto `Cultura` com os dados fornecidos, formatando a string da cultura.
        
        Args:
            data (dict): Dados para atualizar a cultura.
        """
        self.cultura = formatar_string(data['cultura'])
        self.area = data['area']
