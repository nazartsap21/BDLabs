from flask import Blueprint, request, jsonify
from flasgger import swag_from
from src.accuweather.services.location_has_cataclysm_service import LocationHasCataclysmService
from src.accuweather.dao.location_has_cataclysm_dao import LocationHasCataclysmDao
from src import db

location_has_cataclysm_bp = Blueprint('location_has_cataclysm_bp', __name__)
location_has_cataclysm_dao = LocationHasCataclysmDao(db.session)
location_has_cataclysm_service = LocationHasCataclysmService(location_has_cataclysm_dao)


@location_has_cataclysm_bp.route('/location_has_cataclysms', methods=['POST'])
@swag_from({
    'tags': ['LocationHasCataclysms'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'location_id': {'type': 'integer'},
                    'cataclysm_id': {'type': 'integer'}
                },
                'required': ['location_id', 'cataclysm_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'LocationHasCataclysm created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'location_id': {'type': 'integer'},
                    'cataclysm_id': {'type': 'integer'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_location_has_cataclysm_route():
    data = request.get_json()
    new_location_has_cataclysm = location_has_cataclysm_service.create_location_has_cataclysm(data['location_id'], data['cataclysm_id'])
    return jsonify(new_location_has_cataclysm.serialize()), 201


@location_has_cataclysm_bp.route('/location_has_cataclysms', methods=['GET'])
@swag_from({
    'tags': ['LocationHasCataclysms'],
    'responses': {
        200: {
            'description': 'A list of location_has_cataclysms',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'location_id': {'type': 'integer'},
                        'cataclysm_id': {'type': 'integer'}
                    }
                }
            }
        }
    }
})
def get_all_location_has_cataclysms_route():
    location_has_cataclysms = location_has_cataclysm_service.get_all_location_has_cataclysms()
    return jsonify([location_has_cataclysm.serialize() for location_has_cataclysm in location_has_cataclysms])


@location_has_cataclysm_bp.route('/location_has_cataclysms/<int:id>/<int:location_id>/<int:cataclysm_id>', methods=['GET'])
@swag_from({
    'tags': ['LocationHasCataclysms'],
    'responses': {
        200: {
            'description': 'A single location_has_cataclysm',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'location_id': {'type': 'integer'},
                    'cataclysm_id': {'type': 'integer'}
                }
            }
        },
        404: {
            'description': 'LocationHasCataclysm not found'
        }
    }
})
def get_location_has_cataclysm_route(id, location_id, cataclysm_id):
    location_has_cataclysm = location_has_cataclysm_service.get_location_has_cataclysm(id, location_id, cataclysm_id)
    return jsonify(location_has_cataclysm.serialize())


@location_has_cataclysm_bp.route('/location_has_cataclysms/<int:id>/<int:location_id>/<int:cataclysm_id>', methods=['PUT'])
@swag_from({
    'tags': ['LocationHasCataclysms'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'location_id': {'type': 'integer'},
                    'cataclysm_id': {'type': 'integer'}
                },
                'required': ['location_id', 'cataclysm_id']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'LocationHasCataclysm updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'location_id': {'type': 'integer'},
                    'cataclysm_id': {'type': 'integer'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        },
        404: {
            'description': 'LocationHasCataclysm not found'
        }
    }
})
def update_location_has_cataclysm_route(id, location_id, cataclysm_id):
    data = request.get_json()
    location_has_cataclysm = location_has_cataclysm_service.update_location_has_cataclysm(id, location_id, cataclysm_id, data['location_id'], data['cataclysm_id'])
    return jsonify(location_has_cataclysm.serialize())


@location_has_cataclysm_bp.route('/location_has_cataclysms/<int:id>/<int:location_id>/<int:cataclysm_id>', methods=['DELETE'])
@swag_from({
    'tags': ['LocationHasCataclysms'],
    'responses': {
        204: {
            'description': 'LocationHasCataclysm deleted successfully'
        },
        404: {
            'description': 'LocationHasCataclysm not found'
        }
    }
})
def delete_location_has_cataclysm_route(id, location_id, cataclysm_id):
    location_has_cataclysm_service.delete_location_has_cataclysm(id, location_id, cataclysm_id)
    return 'LocationHasCataclysm is deleted', 204
