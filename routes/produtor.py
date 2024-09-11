from flask import Blueprint, request, jsonify
from models.produtor import Produtor, db
from utils.validation import validar_dados

produtor_bp = Blueprint('produtor', __name__, url_prefix='/produtor')

@produtor_bp.route('/', methods=['GET'])
def produtor():
    return jsonify({"message": "Teste"}), 200