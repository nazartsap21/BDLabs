from flask import Blueprint, request, jsonify
from src.accuweather.services.location_has_cataclysm_service import LocationHasCataclysmService
from src.accuweather.dao.location_has_cataclysm_dao import LocationHasCataclysmDao
from src import db

location_has_cataclysm_bp = Blueprint('location_has_cataclysm_bp', __name__)
location_has_cataclysm_dao = LocationHasCataclysmDao(db.session)
location_has_cataclysm_service = LocationHasCataclysmService(location_has_cataclysm_dao)


@location_has_cataclysm_bp.route('/location_has_cataclysms', methods=['POST'])
def create_location_has_cataclysm_route():
    data = request.get_json()
    new_location_has_cataclysm = location_has_cataclysm_service.create_location_has_cataclysm(data['location_id'], data['cataclysm_id'])
    return jsonify(new_location_has_cataclysm.serialize()), 201


@location_has_cataclysm_bp.route('/location_has_cataclysms', methods=['GET'])
def get_all_location_has_cataclysms_route():
    location_has_cataclysms = location_has_cataclysm_service.get_all_location_has_cataclysms()
    return jsonify([location_has_cataclysm.serialize() for location_has_cataclysm in location_has_cataclysms])


@location_has_cataclysm_bp.route('/location_has_cataclysms/<int:id>/<int:location_id>/<int:cataclysm_id>', methods=['GET'])
def get_location_has_cataclysm_route(id, location_id, cataclysm_id):
    location_has_cataclysm = location_has_cataclysm_service.get_location_has_cataclysm(id, location_id, cataclysm_id)
    return jsonify(location_has_cataclysm.serialize())


@location_has_cataclysm_bp.route('/location_has_cataclysms/<int:id>/<int:location_id>/<int:cataclysm_id>', methods=['PUT'])
def update_location_has_cataclysm_route(id, location_id, cataclysm_id):
    data = request.get_json()
    location_has_cataclysm = location_has_cataclysm_service.update_location_has_cataclysm(id, location_id, cataclysm_id, data['location_id'], data['cataclysm_id'])
    return jsonify(location_has_cataclysm.serialize())


@location_has_cataclysm_bp.route('/location_has_cataclysms/<int:id>/<int:location_id>/<int:cataclysm_id>', methods=['DELETE'])
def delete_location_has_cataclysm_route(id, location_id, cataclysm_id):
    location_has_cataclysm_service.delete_location_has_cataclysm(id, location_id, cataclysm_id)
    return 'LocationHasCataclysm is deleted', 204
