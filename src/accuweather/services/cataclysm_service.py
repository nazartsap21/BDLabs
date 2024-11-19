from src.accuweather.dao.cataclysm_dao import CataclysmDao


class CataclysmService:
    def __init__(self, cataclysm_dao: CataclysmDao):
        self.cataclysm_dao = cataclysm_dao

    def create_cataclysm(self, title: str, description: str, start_date: str, end_date: str):
        """Create a new cataclysm."""
        return self.cataclysm_dao.create_cataclysm(title, description, start_date, end_date)

    def get_all_cataclysms(self):
        """Retrieve all cataclysms."""
        return self.cataclysm_dao.get_all_cataclysms()

    def get_cataclysm(self, id: int):
        """Retrieve a cataclysm by ID."""
        return self.cataclysm_dao.get_cataclysm(id)

    def update_cataclysm(self, id: int, title: str, description: str, start_date: str, end_date: str):
        """Update a cataclysm's details."""
        return self.cataclysm_dao.update_cataclysm(id, title, description, start_date, end_date)

    def delete_cataclysm(self, id: int):
        """Delete a cataclysm by ID."""
        return self.cataclysm_dao.delete_cataclysm(id)

    def get_locations_by_cataclysm(self, id: int):
        """Retrieve all locations by cataclysm."""
        return self.cataclysm_dao.get_locations_by_cataclysm(id)