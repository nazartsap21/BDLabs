from flask import Blueprint, request, jsonify
from src.accuweather.services.city_service import CityService
from src.accuweather.dao.city_dao import CityDao
from src import db

city_bp = Blueprint('city_bp', __name__)
city_dao = CityDao(db.session)
city_service = CityService(city_dao)


@city_bp.route('/cities', methods=['POST'])
def create_city_route():
    data = request.get_json()
    new_city = city_service.create_city(data['name'], data['region'], data['country_id'])
    return jsonify(new_city.serialize()), 201


@city_bp.route('/cities', methods=['GET'])
def get_all_cities_route():
    cities = city_service.get_all_cities()
    return jsonify([city.serialize() for city in cities])


@city_bp.route('/cities/<int:id>/<int:country_id>', methods=['GET'])
def get_city_route(id, country_id):
    city = city_service.get_city(id, country_id)
    return jsonify(city.serialize())


@city_bp.route('/cities/<int:id>/<int:country_id>', methods=['PUT'])
def update_city_route(id, country_id):
    data = request.get_json()
    city = city_service.update_city(id, country_id, data['name'], data['region'], data['country_id'])
    return jsonify(city.serialize())


@city_bp.route('/cities/<int:id>/<int:country_id>', methods=['DELETE'])
def delete_city_route(id, country_id):
    city_service.delete_city(id, country_id)
    return 'City is deleted', 204


@city_bp.route('/cities/<int:id>/locations', methods=['GET'])
def get_locations_by_city_route(id):
    locations = city_service.get_locations_by_city(id)
    return jsonify([location.serialize() for location in locations])