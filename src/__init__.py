import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import yaml

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)
    config_path = os.path.join(os.path.dirname(__file__), '../config/app.yml')
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['db']['uri']

    db.init_app(app)

    from src.accuweather.controller.country_controller import country_bp
    from src.accuweather.controller.cataclysm_controller import cataclysm_bp
    from src.accuweather.controller.weather_label_controller import weather_label_bp
    from src.accuweather.controller.city_controller import city_bp
    from src.accuweather.controller.location_controller import location_bp
    from src.accuweather.controller.location_has_cataclysm_controller import location_has_cataclysm_bp
    app.register_blueprint(country_bp)
    app.register_blueprint(cataclysm_bp)
    app.register_blueprint(weather_label_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(location_has_cataclysm_bp)

    @app.route('/ping')
    def hello_world():
        return 'pong'

    return app