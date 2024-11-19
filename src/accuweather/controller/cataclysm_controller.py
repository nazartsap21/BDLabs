from flask import Blueprint, request, jsonify
from src.accuweather.services.cataclysm_service import CataclysmService
from src.accuweather.dao.cataclysm_dao import CataclysmDao
from src import db


cataclysm_bp = Blueprint('cataclysm_bp', __name__)
cataclysm_dao = CataclysmDao(db.session)
cataclysm_service = CataclysmService(cataclysm_dao)


@cataclysm_bp.route('/cataclysms', methods=['POST'])
def create_cataclysm_route():
    data = request.get_json()
    new_cataclysm = cataclysm_service.create_cataclysm(data['title'], data['description'], data['start_date'], data['end_date'])
    return jsonify(new_cataclysm.serialize()), 201


@cataclysm_bp.route('/cataclysms', methods=['GET'])
def get_all_cataclysms_route():
    cataclysms = cataclysm_service.get_all_cataclysms()
    return jsonify([cataclysm.serialize() for cataclysm in cataclysms])


@cataclysm_bp.route('/cataclysms/<int:id>', methods=['GET'])
def get_cataclysm_route(id):
    cataclysm = cataclysm_service.get_cataclysm(id)
    return jsonify(cataclysm.serialize())


@cataclysm_bp.route('/cataclysms/<int:id>', methods=['PUT'])
def update_cataclysm_route(id):
    data = request.get_json()
    cataclysm = cataclysm_service.update_cataclysm(id, data['title'], data['description'], data['start_date'], data['end_date'])
    return jsonify(cataclysm.serialize())


@cataclysm_bp.route('/cataclysms/<int:id>', methods=['DELETE'])
def delete_cataclysm_route(id):
    cataclysm_service.delete_cataclysm(id)
    return 'Cataclysm is deleted', 204


@cataclysm_bp.route('/cataclysms/<int:id>/locations', methods=['GET'])
def get_locations_by_cataclysm_route(id):
    locations = cataclysm_service.get_locations_by_cataclysm(id)
    return jsonify([location.serialize() for location in locations])