from flask import Blueprint, request, jsonify
from src.accuweather.services.country_service import CountryService
from src.accuweather.dao.country_dao import CountryDao
from src import db

country_bp = Blueprint('country_bp', __name__)
country_dao = CountryDao(db.session)
country_service = CountryService(country_dao)


@country_bp.route('/countries', methods=['GET'])
def get_all_countries_route():
    countries = country_service.get_all_countries()
    return jsonify([country.serialize() for country in countries])


@country_bp.route('/countries', methods=['POST'])
def create_country_route():
    data = request.get_json()
    name = data.get('name')
    continent = data.get('continent')
    new_country = country_service.create_country(name, continent)
    return jsonify(new_country.serialize()), 201


@country_bp.route('/countries/<int:id>', methods=['GET'])
def get_country_route(id):
    country = country_service.get_country(id)
    return jsonify(country.serialize())


@country_bp.route('/countries/<int:id>', methods=['PUT'])
def update_country_route(id):
    data = request.get_json()
    country = country_service.update_country(id, data['name'], data['continent'])
    return jsonify(country.serialize())


@country_bp.route('/countries/<int:id>', methods=['DELETE'])
def delete_country_route(id):
    deleted_country = country_service.delete_country(id)
    if deleted_country:
        return jsonify({'message': 'Country deleted successfully'}), 200
    else:
        return jsonify({'message': 'Country not found'}), 404


@country_bp.route('/countries/<int:id>/cities', methods=['GET'])
def get_cities_by_country_route(id):
    cities = country_service.get_cities_by_country(id)
    return jsonify([city.serialize() for city in cities])