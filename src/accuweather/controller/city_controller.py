from flask import Blueprint, request, jsonify
from flasgger import swag_from
from src.accuweather.services.city_service import CityService
from src.accuweather.dao.city_dao import CityDao
from src import db

city_bp = Blueprint('city_bp', __name__)
city_dao = CityDao(db.session)
city_service = CityService(city_dao)


@city_bp.route('/cities', methods=['POST'])
@swag_from({
    'tags': ['Cities'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'region': {'type': 'string'},
                    'country_id': {'type': 'integer'}
                },
                'required': ['name', 'region', 'country_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'City created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'region': {'type': 'string'},
                    'country_id': {'type': 'integer'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_city_route():
    data = request.get_json()
    new_city = city_service.create_city(data['name'], data['region'], data['country_id'])
    return jsonify(new_city.serialize()), 201


@city_bp.route('/cities', methods=['GET'])
@swag_from({
    'tags': ['Cities'],
    'responses': {
        200: {
            'description': 'A list of cities',
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
        }
    }
})
def get_all_cities_route():
    cities = city_service.get_all_cities()
    return jsonify([city.serialize() for city in cities])


@city_bp.route('/cities/<int:id>/<int:country_id>', methods=['GET'])
@swag_from({
    'tags': ['Cities'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the city'
        },
        {
            'name': 'country_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the country'
        }
    ],
    'responses': {
        200: {
            'description': 'City details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'region': {'type': 'string'},
                    'country_id': {'type': 'integer'}
                }
            }
        },
        404: {
            'description': 'City not found'
        }
    }
})
def get_city_route(id, country_id):
    city = city_service.get_city(id, country_id)
    return jsonify(city.serialize())


@city_bp.route('/cities/<int:id>/<int:country_id>', methods=['PUT'])
@swag_from({
    'tags': ['Cities'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the city to update'
        },
        {
            'name': 'country_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the country'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'region': {'type': 'string'},
                    'country_id': {'type': 'integer'}
                },
                'required': ['name', 'region', 'country_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'City updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'region': {'type': 'string'},
                    'country_id': {'type': 'integer'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        },
        404: {
            'description': 'City not found'
        }
    }
})
def update_city_route(id, country_id):
    data = request.get_json()
    city = city_service.update_city(id, country_id, data['name'], data['region'], data['country_id'])
    return jsonify(city.serialize())


@city_bp.route('/cities/<int:id>/<int:country_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Cities'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the city to delete'
        },
        {
            'name': 'country_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the country'
        }
    ],
    'responses': {
        204: {
            'description': 'City deleted successfully'
        },
        404: {
            'description': 'City not found'
        }
    }
})
def delete_city_route(id, country_id):
    city_service.delete_city(id, country_id)
    return 'City is deleted', 204


@city_bp.route('/cities/<int:id>/locations', methods=['GET'])
@swag_from({
    'tags': ['Cities'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the city'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of locations for the specified city',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'latitude': {'type': 'number'},
                        'longitude': {'type': 'number'},
                        'city_id': {'type': 'integer'}
                    }
                }
            }
        },
        404: {
            'description': 'City not found'
        }
    }
})
def get_locations_by_city_route(id):
    locations = city_service.get_locations_by_city(id)
    return jsonify([location.serialize() for location in locations])