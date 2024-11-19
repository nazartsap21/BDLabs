from src.accuweather.dao.country_dao import CountryDao

class CountryService:
    def __init__(self, country_dao: CountryDao):
        self.country_dao = country_dao

    def create_country(self, name: str, continent: str):
        """Create a new country."""
        return self.country_dao.create_country(name, continent)

    def get_all_countries(self):
        """Retrieve all countries."""
        return self.country_dao.get_all_countries()

    def get_country(self, id: int):
        """Retrieve a country by ID."""
        return self.country_dao.get_country(id)

    def update_country(self, id: int, name: str, continent: str):
        """Update a country's details."""
        return self.country_dao.update_country(id, name, continent)

    def delete_country(self, id: int):
        """Delete a country by ID."""
        return self.country_dao.delete_country(id)

    def get_cities_by_country(self, id: int):
        """Retrieve all cities in a country."""
        return self.country_dao.get_cities_by_country(id)