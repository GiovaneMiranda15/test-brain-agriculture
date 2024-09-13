from flask import Blueprint, request, jsonify
from models.produtor import Produtor, Cultura, db

# Define o Blueprint para o dashboard
dashboard_bp = Blueprint('dashboard', __name__, url_prefix="/dashboard")

@dashboard_bp.route('/', methods=['GET'])
def dashboard():
    """
    Retorna as estatísticas do dashboard, incluindo:
    - Total de fazendas
    - Total de área das fazendas
    - Total de fazendas por estado
    - Total de culturas plantadas
    - Uso do solo (área agricultável e vegetação)
    """
    try:
        # Total de fazendas
        total_fazendas = Produtor.query.count()

        # Total de área
        total_area = db.session.query(db.func.sum(Produtor.area_total)).scalar() or 0

        # Total por estado
        estados = db.session.query(Produtor.estado, db.func.count(Produtor.estado)) \
            .group_by(Produtor.estado).all()
        estados_dict = {estado: count for estado, count in estados}

        # Total por cultura
        culturas = db.session.query(Cultura.cultura, db.func.count(Cultura.cultura)) \
            .join(Produtor, Cultura.produtor_id == Produtor.id) \
            .group_by(Cultura.cultura).all()
        culturas_dict = {cultura: count for cultura, count in culturas}

        # Uso do solo
        uso_solo = {
            "Agricultável": db.session.query(db.func.sum(Produtor.area_agricultavel)).scalar() or 0,
            "Vegetação": db.session.query(db.func.sum(Produtor.area_vegetacao)).scalar() or 0
        }

        # Retorna os dados do dashboard em formato JSON
        return jsonify({"status": True,
            "data": {
                "total_fazendas": total_fazendas,
                "total_area": float(total_area),
                "estados": estados_dict,
                "culturas": culturas_dict,
                "uso_solo": uso_solo
            }
        }), 200

    except Exception as e:
        # Em caso de erro, retorna a mensagem de erro
        return jsonify({"status": False, "message": str(e)}), 400
