from src.accuweather.domain.models import City, Location

class CityDao:
    def __init__(self, session):
        self.session = session

    def create_city(self, name, region, country_id):
        new_city = City(name=name, region=region, country_id=country_id)
        self.session.add(new_city)
        self.session.commit()
        return new_city

    def get_all_cities(self):
        return self.session.query(City).all()

    def get_city(self, id, country_id):
        return self.session.query(City).filter_by(id=id, country_id=country_id).first()

    def update_city(self, id, country_id, name, region, new_country_id):
        city = self.session.query(City).filter_by(id=id, country_id=country_id).first()
        if city:
            city.name = name
            city.region = region
            city.country_id = new_country_id
            self.session.commit()
        return city

    def delete_city(self, id, country_id):
        city = self.session.query(City).filter_by(id=id, country_id=country_id).first()
        if city:
            self.session.delete(city)
            self.session.commit()
        return city

    def get_locations_by_city(self, id):
        return self.session.query(Location).filter_by(city_id=id).all()