from flask import Blueprint, request, jsonify
from flasgger import swag_from
from src.accuweather.services.country_service import CountryService
from src.accuweather.dao.country_dao import CountryDao
from src import db

country_bp = Blueprint('country_bp', __name__)
country_dao = CountryDao(db.session)
country_service = CountryService(country_dao)


@country_bp.route('/countries', methods=['GET'])
@swag_from({
    'tags': ['Countries'],
    'responses': {
        200: {
            'description': 'A list of countries',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'continent': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def get_all_countries_route():
    countries = country_service.get_all_countries()
    return jsonify([country.serialize() for country in countries])


@country_bp.route('/countries', methods=['POST'])
@swag_from({
    'tags': ['Countries'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'continent': {'type': 'string'}
                },
                'required': ['name', 'continent']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Country created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'continent': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_country_route():
    data = request.get_json()
    name = data.get('name')
    continent = data.get('continent')
    new_country = country_service.create_country(name, continent)
    return jsonify(new_country.serialize()), 201


@country_bp.route('/countries/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Countries'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the country to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Country details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'continent': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'Country not found'
        }
    }
})
def get_country_route(id):
    country = country_service.get_country(id)
    return jsonify(country.serialize())


@country_bp.route('/countries/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Countries'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the country to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'continent': {'type': 'string'}
                },
                'required': ['name', 'continent']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Country updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'continent': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        },
        404: {
            'description': 'Country not found'
        }
    }
})
def update_country_route(id):
    data = request.get_json()
    country = country_service.update_country(id, data['name'], data['continent'])
    return jsonify(country.serialize())


@country_bp.route('/countries/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Countries'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the country to delete'
        }
    ],
    'responses': {
        200: {
            'description': 'Country deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'Country not found'
        }
    }
})
def delete_country_route(id):
    deleted_country = country_service.delete_country(id)
    if deleted_country:
        return jsonify({'message': 'Country deleted successfully'}), 200
    else:
        return jsonify({'message': 'Country not found'}), 404


@country_bp.route('/countries/<int:id>/cities', methods=['GET'])
@swag_from({
    'tags': ['Countries'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the country to retrieve cities for'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of cities in the specified country',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'region': {'type': 'string'},
                        'country_id': {'type': 'integer'}
                    }
                }
            }
        },
        404: {
            'description': 'Country not found'
        }
    }
})
def get_cities_by_country_route(id):
    cities = country_service.get_cities_by_country(id)
    return jsonify([city.serialize() for city in cities])