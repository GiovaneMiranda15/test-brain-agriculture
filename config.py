import os

# Obtém a URL de conexão do banco de dados a partir das variáveis de ambiente.
# Se a variável de ambiente DATABASE_URL não estiver definida, utiliza o valor padrão fornecido.
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/agricultura')
