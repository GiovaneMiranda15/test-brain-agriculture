from flask import Blueprint, request, jsonify
from models.produtor import Produtor, Cultura, db
from utils.validation import validar_dados

# Define o Blueprint para as rotas de Produtor
produtor_bp = Blueprint('produtor', __name__, url_prefix='/produtor')

@produtor_bp.route('/', methods=['POST'])
def adicionar():
    """
    Adiciona um novo produtor ao banco de dados.
    """
    data = request.get_json()
    try:
        # Cria um novo objeto Produtor com os dados recebidos
        produtor = Produtor(
            cpf_cnpj=data['cpf_cnpj'],
            nome_produtor=data['nome_produtor'],
            nome_fazenda=data['nome_fazenda'],
            cidade=data['cidade'],
            estado=data['estado'],
            area_total=data['area_total'],
            area_agricultavel=data['area_agricultavel'],
            area_vegetacao=data['area_vegetacao'],
        )
        
        # Adiciona as culturas associadas ao produtor
        for cultura_data in data['culturas']:
            cultura = Cultura(
                cultura=cultura_data['cultura'],
                area=cultura_data['area']
            )
            produtor.culturas.append(cultura)
        
        # Valida os dados do produtor
        validar_dados(produtor.to_dict())
        
        # Adiciona o produtor ao banco de dados e confirma a transação
        db.session.add(produtor)
        db.session.commit()
        return jsonify({"message": "Cadastro realizado com sucesso", "data": produtor.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@produtor_bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    """
    Atualiza um produtor existente no banco de dados.
    """
    data = request.get_json()
    try:
        # Recupera o produtor pelo ID, ou retorna 404 se não encontrado
        produtor = Produtor.query.get_or_404(id)
        
        # Atualiza as informações do produtor
        produtor.cpf_cnpj = data['cpf_cnpj']
        produtor.nome_produtor = data['nome_produtor']
        produtor.nome_fazenda = data['nome_fazenda']
        produtor.cidade = data['cidade']
        produtor.estado = data['estado']
        produtor.area_total = data['area_total']
        produtor.area_agricultavel = data['area_agricultavel']
        produtor.area_vegetacao = data['area_vegetacao']
        
        # Atualiza ou adiciona culturas
        culturas_data = data.get('culturas', [])
        culturas_existentes = {cultura.cultura: cultura for cultura in produtor.culturas}
        culturas_atualizadas = set()

        for cultura_data in culturas_data:
            nome_cultura = cultura_data['cultura']
            area_cultura = cultura_data['area']
            culturas_atualizadas.add(nome_cultura)
            
            if nome_cultura in culturas_existentes:
                # Atualiza a cultura existente
                cultura_existente = culturas_existentes[nome_cultura]
                cultura_existente.area = area_cultura
            else:
                # Adiciona nova cultura
                nova_cultura = Cultura(
                    cultura=nome_cultura,
                    area=area_cultura
                )
                produtor.culturas.append(nova_cultura)

        # Remove culturas que não foram incluídas na atualização
        for cultura_nome in culturas_existentes:
            if cultura_nome not in culturas_atualizadas:
                db.session.delete(culturas_existentes[cultura_nome])
        
        # Valida os dados atualizados do produtor
        validar_dados(produtor.to_dict())
        
        # Confirma as alterações no banco de dados
        db.session.commit()
        return jsonify({"message": "Atualização realizada com sucesso", "data": produtor.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@produtor_bp.route('/', methods=['GET'])
def buscar():
    """
    Busca todos os produtores no banco de dados.
    """
    try:
        # Recupera todos os produtores
        produtores = Produtor.query.all()
        return jsonify({"message": "Busca realizada com sucesso", "data": [produtor.to_dict() for produtor in produtores]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@produtor_bp.route('/<int:id>', methods=['GET'])
def buscar_id(id):
    """
    Busca um produtor pelo ID.
    """
    try:
        # Recupera o produtor pelo ID, ou retorna 404 se não encontrado
        produtor = Produtor.query.get_or_404(id)
        return jsonify({"message": "Busca realizada com sucesso", "data": produtor.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@produtor_bp.route('/<int:id>', methods=['DELETE'])
def excluir(id):
    """
    Remove um produtor do banco de dados pelo ID.
    """
    try:
        # Recupera o produtor pelo ID, ou retorna 404 se não encontrado
        produtor = Produtor.query.get_or_404(id)
        
        # Remove o produtor do banco de dados
        db.session.delete(produtor)
        db.session.commit()
        
        return jsonify({"message": "Produtor excluído com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
