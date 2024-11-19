from src.accuweather.domain.models import Location, Cataclysm, LocationHasCataclysm


class LocationDao:
    def __init__(self, session):
        self.session = session

    def create_location(self, latitude, longitude, has_water_body, city_id):
        new_location = Location(latitude=latitude, longitude=longitude, has_water_body=has_water_body, city_id=city_id)
        self.session.add(new_location)
        self.session.commit()
        return new_location

    def get_all_locations(self):
        return self.session.query(Location).all()

    def get_location(self, id):
        return self.session.query(Location).get(id)

    def update_location(self, id, latitude, longitude, has_water_body, city_id):
        location = self.session.query(Location).get(id)
        if location:
            location.latitude = latitude
            location.longitude = longitude
            location.has_water_body = has_water_body
            location.city_id = city_id
            self.session.commit()
        return location

    def delete_location(self, id):
        location = self.session.query(Location).get(id)
        if location:
            self.session.delete(location)
            self.session.commit()
        return location

    def get_cataclysms_by_location(self, id):
        return self.session.query(Cataclysm).join(LocationHasCataclysm, Cataclysm.id == LocationHasCataclysm.cataclysm_id).filter(LocationHasCataclysm.location_id == id).all()