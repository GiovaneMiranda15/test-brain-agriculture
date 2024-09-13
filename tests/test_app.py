import pytest
from app import app, db
from models.produtor import Produtor, Cultura

@pytest.fixture
def client():
    """
    Fixture para configurar o cliente de teste e o banco de dados em memória.
    """
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Usando SQLite em memória para testes

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria as tabelas no banco de dados em memória
        yield client
        with app.app_context():
            db.drop_all()  # Limpa o banco de dados após os testes

def test_adicionar_produtor(client):
    """
    Testa o endpoint de adição de produtores. Verifica se o produtor é adicionado corretamente.
    """
    response = client.post('/produtor/', json={
        "cpf_cnpj": "91398622087",
        "nome_produtor": "Marcelo",
        "nome_fazenda": "Fazenda Silva",
        "cidade": "São Paulo",
        "estado": "SP",
        "area_total": 100.0,
        "area_agricultavel": 80.0,
        "area_vegetacao": 20.0,
        "culturas": [
            {"cultura": "Soja", "area": 40.0},
            {"cultura": "Milho", "area": 40.0}
        ]
    })
    assert response.status_code == 200
    assert b"FAZENDA SILVA" in response.data

def test_buscar_produtores(client):
    """
    Testa o endpoint de busca de todos os produtores. Verifica se a lista de produtores é retornada corretamente.
    """
    # Primeiro, adicione um produtor
    client.post('/produtor/', json={
        "cpf_cnpj": "91398622087",
        "nome_produtor": "Marcelo",
        "nome_fazenda": "Fazenda Silva",
        "cidade": "São Paulo",
        "estado": "SP",
        "area_total": 100.0,
        "area_agricultavel": 80.0,
        "area_vegetacao": 20.0,
        "culturas": [
            {"cultura": "Soja", "area": 40.0},
            {"cultura": "Milho", "area": 40.0}
        ]
    })

    response = client.get('/produtor/')
    assert response.status_code == 200
    assert b"MARCELO" in response.data

def test_buscar_produtor_por_id(client):
    """
    Testa o endpoint de busca de um produtor por ID. Verifica se o produtor específico é retornado corretamente.
    """
    # Adiciona um produtor
    response = client.post('/produtor/', json={
        "cpf_cnpj": "91398622087",
        "nome_produtor": "Marcelo",
        "nome_fazenda": "Fazenda Silva",
        "cidade": "São Paulo",
        "estado": "SP",
        "area_total": 100.0,
        "area_agricultavel": 80.0,
        "area_vegetacao": 20.0,
        "culturas": [
            {"cultura": "Soja", "area": 40.0},
            {"cultura": "Milho", "area": 40.0}
        ]
    })
    produtor_id = response.json['data']['id']

    # Busca o produtor por ID
    response = client.get(f'/produtor/{produtor_id}')
    assert response.status_code == 200
    assert b"MARCELO" in response.data

def test_atualizar_produtor(client):
    """
    Testa o endpoint de atualização de um produtor. Verifica se o produtor é atualizado corretamente.
    """
    # Adiciona um produtor
    response = client.post('/produtor/', json={
        "cpf_cnpj": "91398622087",
        "nome_produtor": "Marcelo",
        "nome_fazenda": "Fazenda Silva",
        "cidade": "São Paulo",
        "estado": "SP",
        "area_total": 100.0,
        "area_agricultavel": 80.0,
        "area_vegetacao": 20.0,
        "culturas": [
            {"cultura": "Soja", "area": 40.0},
            {"cultura": "Milho", "area": 40.0}
        ]
    })
    produtor_id = response.json['data']['id']

    # Atualiza o produtor
    response = client.put(f'/produtor/{produtor_id}', json={
        "cpf_cnpj": "91398622087",
        "nome_produtor": "Marcelo Atualizado",
        "nome_fazenda": "Fazenda Silva Atualizada",
        "cidade": "São Paulo",
        "estado": "SP",
        "area_total": 100.0,
        "area_agricultavel": 70.0,
        "area_vegetacao": 30.0,
        "culturas": [
            {"cultura": "Soja", "area": 35.0},
            {"cultura": "Milho", "area": 35.0},
            {"cultura": "Café", "area": 30.0}
        ]
    })
    assert response.status_code == 200
    assert b"MARCELO ATUALIZADO" in response.data

def test_excluir_produtor(client):
    """
    Testa o endpoint de exclusão de um produtor. Verifica se o produtor é excluído corretamente.
    """
    # Adiciona um produtor
    response = client.post('/produtor/', json={
        "cpf_cnpj": "91398622087",
        "nome_produtor": "Marcelo",
        "nome_fazenda": "Fazenda Silva",
        "cidade": "São Paulo",
        "estado": "SP",
        "area_total": 100.0,
        "area_agricultavel": 80.0,
        "area_vegetacao": 20.0,
        "culturas": [
            {"cultura": "Soja", "area": 40.0},
            {"cultura": "Milho", "area": 40.0}
        ]
    })

    # Busca o produtor
    response = client.get('/produtor/')
    produtor_id = response.json['data'][0]['id']

    # Exclui o produtor
    response = client.delete(f'/produtor/{produtor_id}')
    assert response.status_code == 200
    assert b"sucesso" in response.data

    # Verifica se o produtor foi excluído
    response = client.get('/produtor/')
    assert b"MARCELO" not in response.data
