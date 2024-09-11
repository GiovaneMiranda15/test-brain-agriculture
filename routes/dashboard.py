from flask import Blueprint, request, jsonify
from models.produtor import Produtor, db

dashboard_bp = Blueprint('dashboard', __name__, url_prefix="/dashboard")

@dashboard_bp.route('/', methods=['GET'])
def dashboard():
    return jsonify({"message": "Testedashboard"}), 200