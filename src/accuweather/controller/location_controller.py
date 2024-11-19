from flask import Blueprint, request, jsonify
from src.accuweather.services.location_service import LocationService
from src.accuweather.dao.location_dao import LocationDao
from src import db

location_bp = Blueprint('location_bp', __name__)
location_dao = LocationDao(db.session)
location_service = LocationService(location_dao)


@location_bp.route('/locations', methods=['POST'])
def create_location_route():
    data = request.get_json()
    new_location = location_service.create_location(data['latitude'], data['longitude'], data['has_water_body'], data['city_id'])
    return jsonify(new_location.serialize()), 201


@location_bp.route('/locations', methods=['GET'])
def get_all_locations_route():
    locations = location_service.get_all_locations()
    return jsonify([location.serialize() for location in locations])


@location_bp.route('/locations/<int:id>', methods=['GET'])
def get_location_route(id):
    location = location_service.get_location(id)
    return jsonify(location.serialize())


@location_bp.route('/locations/<int:id>', methods=['PUT'])
def update_location_route(id):
    data = request.get_json()
    location = location_service.update_location(id, **data)
    return jsonify(location.serialize())


@location_bp.route('/locations/<int:id>', methods=['DELETE'])
def delete_location_route(id):
    location_service.delete_location(id)
    return 'Location is deleted', 204


@location_bp.route('/locations/<int:id>/cataclysms', methods=['GET'])
def get_cataclysms_by_location_route(id):
    cataclysms = location_service.get_cataclysms_by_location(id)
    return jsonify([cataclysm.serialize() for cataclysm in cataclysms])
