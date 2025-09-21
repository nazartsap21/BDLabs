from flask import Blueprint, request, jsonify
from flasgger import swag_from
from src.accuweather.services.location_service import LocationService
from src.accuweather.dao.location_dao import LocationDao
from src import db

location_bp = Blueprint('location_bp', __name__)
location_dao = LocationDao(db.session)
location_service = LocationService(location_dao)


@location_bp.route('/locations', methods=['POST'])
@swag_from({
    'tags': ['Locations'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'latitude': {'type': 'float'},
                    'longitude': {'type': 'float'},
                    'has_water_body': {'type': 'boolean'},
                    'city_id': {'type': 'integer'}
                },
                'required': ['latitude', 'longitude', 'has_water_body', 'city_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Location created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'latitude': {'type': 'float'},
                    'longitude': {'type': 'float'},
                    'has_water_body': {'type': 'boolean'},
                    'city_id': {'type': 'integer'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_location_route():
    data = request.get_json()
    new_location = location_service.create_location(data['latitude'], data['longitude'], data['has_water_body'], data['city_id'])
    return jsonify(new_location.serialize()), 201


@location_bp.route('/locations', methods=['GET'])
@swag_from({
    'tags': ['Locations'],
    'responses': {
        200: {
            'description': 'A list of locations',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'latitude': {'type': 'float'},
                        'longitude': {'type': 'float'},
                        'has_water_body': {'type': 'boolean'},
                        'city_id': {'type': 'integer'}
                    }
                }
            }
        }
    }
})
def get_all_locations_route():
    locations = location_service.get_all_locations()
    return jsonify([location.serialize() for location in locations])


@location_bp.route('/locations/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Locations'],
    'responses': {
        200: {
            'description': 'A single location',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'latitude': {'type': 'float'},
                    'longitude': {'type': 'float'},
                    'has_water_body': {'type': 'boolean'},
                    'city_id': {'type': 'integer'}
                }
            }
        },
        404: {
            'description': 'Location not found'
        }
    }
})
def get_location_route(id):
    location = location_service.get_location(id)
    return jsonify(location.serialize())


@location_bp.route('/locations/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Locations'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the location to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'latitude': {'type': 'float'},
                    'longitude': {'type': 'float'},
                    'has_water_body': {'type': 'boolean'},
                    'city_id': {'type':
                        'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Location updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'latitude': {'type': 'float'},
                    'longitude': {'type': 'float'},
                    'has_water_body': {'type': 'boolean'},
                    'city_id': {'type':
                        'integer'}
                }
            }
        },
        404: {
            'description': 'Location not found'
        }
    }
})
def update_location_route(id):
    data = request.get_json()
    location = location_service.update_location(id, **data)
    return jsonify(location.serialize())


@location_bp.route('/locations/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Locations'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the location to delete'
        }
    ],
    'responses': {
        204: {
            'description': 'Location deleted successfully'
        },
        404: {
            'description': 'Location not found'
        }
    }
})
def delete_location_route(id):
    location_service.delete_location(id)
    return 'Location is deleted', 204


@location_bp.route('/locations/<int:id>/cataclysms', methods=['GET'])
@swag_from({
    'tags': ['Locations'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the location to retrieve cataclysms for'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of cataclysms affecting the location',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'description': {'type': 'string'},
                        'start_date': {'type': 'string', 'format': 'date-time'},
                        'end_date': {'type': 'string', 'format': 'date-time'}
                    }
                }
            }
        },
        404: {
            'description': 'Location not found'
        }
    }
})
def get_cataclysms_by_location_route(id):
    cataclysms = location_service.get_cataclysms_by_location(id)
    return jsonify([cataclysm.serialize() for cataclysm in cataclysms])
