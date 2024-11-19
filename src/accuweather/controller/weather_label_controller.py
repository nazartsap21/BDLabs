from flask import Blueprint, request, jsonify
from src.accuweather.services.weather_label_service import WeatherLabelService
from src.accuweather.dao.weather_label_dao import WeatherLabelDao
from src import db

weather_label_bp = Blueprint('weather_label_bp', __name__)
weather_label_dao = WeatherLabelDao(db.session)
weather_label_service = WeatherLabelService(weather_label_dao)


@weather_label_bp.route('/weather_labels', methods=['POST'])
def create_weather_label_route():
    data = request.get_json()
    new_weather_label = weather_label_service.create_weather_label(data['name'], data['link'])
    return jsonify(new_weather_label.serialize()), 201


@weather_label_bp.route('/weather_labels', methods=['GET'])
def get_all_weather_labels_route():
    weather_labels = weather_label_service.get_all_weather_labels()
    return jsonify([weather_label.serialize() for weather_label in weather_labels])


@weather_label_bp.route('/weather_labels/<int:id>', methods=['GET'])
def get_weather_label_route(id):
    weather_label = weather_label_service.get_weather_label(id)
    return jsonify(weather_label.serialize())


@weather_label_bp.route('/weather_labels/<int:id>', methods=['PUT'])
def update_weather_label_route(id):
    data = request.get_json()
    weather_label = weather_label_service.update_weather_label(id, data['name'], data['link'])
    return jsonify(weather_label.serialize())


@weather_label_bp.route('/weather_labels/<int:id>', methods=['DELETE'])
def delete_weather_label_route(id):
    weather_label_service.delete_weather_label(id)
    return 'WeatherLabel is deleted', 204