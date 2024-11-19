# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cataclysm(Base):
    __tablename__ = 'cataclysm'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(45), nullable=False, index=True)
    description = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date
        }


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False, unique=True)
    continent = Column(String(45), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'continent': self.continent
        }


class ForecastPeriod(Base):
    __tablename__ = 'forecast_period'

    id = Column(Integer, primary_key=True)
    period_name = Column(String(45), nullable=False)


class WeatherLabel(Base):
    __tablename__ = 'weather_label'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)
    link = Column(String(100), nullable=False, unique=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link
        }


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    country_id = Column(ForeignKey('country.id'), primary_key=True, nullable=False, index=True)
    name = Column(String(45), nullable=False, index=True)
    region = Column(String(45), nullable=False)

    country = relationship('Country')

    def serialize(self):
        return {
            'id': self.id,
            'country_id': self.country_id,
            'name': self.name,
            'region': self.region
        }



class WeatherCondition(Base):
    __tablename__ = 'weather_condition'

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    precipitation = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    wind_direction = Column(String(45), nullable=False)
    humidity = Column(String(45), nullable=False)
    water_temperature = Column(Float)
    weather_label_id = Column(ForeignKey('weather_label.id'), nullable=False, index=True)

    weather_label = relationship('WeatherLabel')


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(String(45), nullable=False)
    longitude = Column(String(45), nullable=False)
    has_water_body = Column(TINYINT, nullable=False)
    city_id = Column(ForeignKey('city.id'), index=True)

    city = relationship('City')

    def serialize(self):
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'has_water_body': self.has_water_body,
            'city_id': self.city_id
        }


class DailyWeather(Base):
    __tablename__ = 'daily_weather'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    weather_condition_id = Column(ForeignKey('weather_condition.id'), nullable=False, index=True)
    location_id = Column(ForeignKey('location.id'), nullable=False, index=True)

    location = relationship('Location')
    weather_condition = relationship('WeatherCondition')


class HourlyWeather(Base):
    __tablename__ = 'hourly_weather'

    id = Column(Integer, primary_key=True)
    time = Column(String(45))
    weather_condition_id = Column(ForeignKey('weather_condition.id'), nullable=False, index=True)
    location_id = Column(ForeignKey('location.id'), nullable=False, index=True)

    location = relationship('Location')
    weather_condition = relationship('WeatherCondition')


class LocationHasCataclysm(Base):
    __tablename__ = 'location_has_cataclysm'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    location_id = Column(ForeignKey('location.id'), primary_key=True, nullable=False, index=True)
    cataclysm_id = Column(ForeignKey('cataclysm.id'), primary_key=True, nullable=False, index=True)

    cataclysm = relationship('Cataclysm', primaryjoin='LocationHasCataclysm.cataclysm_id == Cataclysm.id')
    location = relationship('Location', primaryjoin='LocationHasCataclysm.location_id == Location.id')

    def serialize(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'cataclysm_id': self.cataclysm_id
        }


class WeatherForecast(Base):
    __tablename__ = 'weather_forecast'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    location_id = Column(ForeignKey('location.id'), nullable=False, index=True)
    weather_condition_id = Column(ForeignKey('weather_condition.id'), nullable=False, index=True)
    forecast_period_id = Column(ForeignKey('forecast_period.id'), nullable=False, index=True)

    forecast_period = relationship('ForecastPeriod')
    location = relationship('Location')
    weather_condition = relationship('WeatherCondition')
