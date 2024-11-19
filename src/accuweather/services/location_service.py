from src.accuweather.dao.location_dao import LocationDao


class LocationService:
    def __init__(self, location_dao: LocationDao):
        self.location_dao = location_dao

    def create_location(self, latitude: str, longitude: str, has_water_body: bool, city_id: int):
        """Create a new location."""
        return self.location_dao.create_location(latitude, longitude, has_water_body, city_id)

    def get_all_locations(self):
        """Retrieve all locations."""
        return self.location_dao.get_all_locations()

    def get_location(self, id: int):
        """Retrieve a location by ID."""
        return self.location_dao.get_location(id)

    def update_location(self, id: int, latitude: str, longitude: str, has_water_body: bool, city_id: int):
        """Update a location's details."""
        return self.location_dao.update_location(id, latitude, longitude, has_water_body, city_id)

    def delete_location(self, id: int):
        """Delete a location by ID."""
        return self.location_dao.delete_location(id)

    def get_cataclysms_by_location(self, id: int):
        """Retrieve all cataclysms by location."""
        return self.location_dao.get_cataclysms_by_location(id)