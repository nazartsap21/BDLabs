from flask import Blueprint, request, jsonify
from flasgger import swag_from
from src.accuweather.services.cataclysm_service import CataclysmService
from src.accuweather.dao.cataclysm_dao import CataclysmDao
from src import db


cataclysm_bp = Blueprint('cataclysm_bp', __name__)
cataclysm_dao = CataclysmDao(db.session)
cataclysm_service = CataclysmService(cataclysm_dao)


@cataclysm_bp.route('/cataclysms', methods=['POST'])
@swag_from({
    'tags': ['Cataclysms'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'start_date': {'type': 'string', 'format': 'date'},
                    'end_date': {'type': 'string', 'format': 'date'}
                },
                'required': ['title', 'description', 'start_date', 'end_date']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Cataclysm created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'start_date': {'type': 'string', 'format': 'date'},
                    'end_date': {'type': 'string', 'format': 'date'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_cataclysm_route():
    data = request.get_json()
    new_cataclysm = cataclysm_service.create_cataclysm(data['title'], data['description'], data['start_date'], data['end_date'])
    return jsonify(new_cataclysm.serialize()), 201


@cataclysm_bp.route('/cataclysms', methods=['GET'])
@swag_from({
    'tags': ['Cataclysms'],
    'responses': {
        200: {
            'description': 'List of cataclysms',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'description': {'type': 'string'},
                        'start_date': {'type': 'string', 'format': 'date'},
                        'end_date': {'type': 'string', 'format': 'date'}
                    }
                }
            }
        }
    }
})
def get_all_cataclysms_route():
    cataclysms = cataclysm_service.get_all_cataclysms()
    return jsonify([cataclysm.serialize() for cataclysm in cataclysms])


@cataclysm_bp.route('/cataclysms/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Cataclysms'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the cataclysm to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Cataclysm details',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'start_date': {'type': 'string', 'format': 'date'},
                    'end_date': {'type': 'string', 'format': 'date'}
                }
            }
        },
        404: {
            'description': 'Cataclysm not found'
        }
    }
})
def get_cataclysm_route(id):
    cataclysm = cataclysm_service.get_cataclysm(id)
    return jsonify(cataclysm.serialize())


@cataclysm_bp.route('/cataclysms/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Cataclysms'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of cataclysm to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'start_date': {'type': 'string', 'format': 'date'},
                    'end_date': {'type': 'string', 'format': 'date'}
                },
                'required': ['title', 'description', 'start_date', 'end_date']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Cataclysm updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'start_date': {'type': 'string', 'format': 'date'},
                    'end_date': {'type': 'string', 'format': 'date'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        },
        404: {
            'description': 'Cataclysm not found'
        }
    }
})
def update_cataclysm_route(id):
    data = request.get_json()
    cataclysm = cataclysm_service.update_cataclysm(id, data['title'], data['description'], data['start_date'], data['end_date'])
    return jsonify(cataclysm.serialize())


@cataclysm_bp.route('/cataclysms/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Cataclysms'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the cataclysm to delete'
        }
    ],
    'responses': {
        204: {
            'description': 'Cataclysm deleted successfully'
        },
        404: {
            'description': 'Cataclysm not found'
        }
    }
})
def delete_cataclysm_route(id):
    cataclysm_service.delete_cataclysm(id)
    return 'Cataclysm is deleted', 204


@cataclysm_bp.route('/cataclysms/<int:id>/locations', methods=['GET'])
@swag_from({
    'tags': ['Cataclysms'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the cataclysm to retrieve locations for'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of locations affected by the cataclysm',
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
            'description': 'Cataclysm not found'
        }
    }
})
def get_locations_by_cataclysm_route(id):
    locations = cataclysm_service.get_locations_by_cataclysm(id)
    return jsonify([location.serialize() for location in locations])