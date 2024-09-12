from flask import Flask
from config import DATABASE_URL
from models.produtor import db
from routes.produtor import produtor_bp
from routes.dashboard import dashboard_bp

def create_app():
    """
    Cria e configura a instância do Flask.
    
    Retorna:
    Flask: A instância configurada do Flask.
    """
    # Cria a aplicação Flask
    app = Flask(__name__)
    
    # Configura a URI do banco de dados e desativa o rastreamento de modificações
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializa a extensão SQLAlchemy com a aplicação
    db.init_app(app)
    
    # Registra os blueprints para rotas de produtor e dashboard
    app.register_blueprint(produtor_bp)
    app.register_blueprint(dashboard_bp)
    
    return app

# Cria a aplicação Flask
app = create_app()

# Executa a aplicação se este módulo for executado como o principal
if __name__ == '__main__':
    # Executa a aplicação com modo de depuração ativado
    app.run(debug=True)
