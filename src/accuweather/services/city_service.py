from src.accuweather.dao.city_dao import CityDao


class CityService:
    def __init__(self, city_dao: CityDao):
        self.city_dao = city_dao

    def create_city(self, name: str, region: str, country_id: int):
        """Create a new city."""
        return self.city_dao.create_city(name, region, country_id)

    def get_all_cities(self):
        """Retrieve all cities."""
        return self.city_dao.get_all_cities()

    def get_city(self, id: int, country_id: int):
        """Retrieve a city by ID."""
        return self.city_dao.get_city(id, country_id)

    def update_city(self, id: int, country_id:int, name: str, region: str, new_country_id: int):
        """Update a city's details."""
        return self.city_dao.update_city(id, country_id, name, region, new_country_id)

    def delete_city(self, id: int, country_id: int):
        """Delete a city by ID."""
        return self.city_dao.delete_city(id, country_id)

    def get_locations_by_city(self, id: int):
        """Retrieve all locations in a city."""
        return self.city_dao.get_locations_by_city(id)