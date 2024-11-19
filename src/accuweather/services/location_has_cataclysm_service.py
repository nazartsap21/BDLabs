from src.accuweather.dao.location_has_cataclysm_dao import LocationHasCataclysmDao


class LocationHasCataclysmService:
    def __init__(self, location_has_cataclysm_dao):
        self.location_has_cataclysm_dao = location_has_cataclysm_dao

    def create_location_has_cataclysm(self, location_id: int, cataclysm_id: int):
        return self.location_has_cataclysm_dao.create_location_has_cataclysm(location_id, cataclysm_id)

    def get_all_location_has_cataclysms(self):
        return self.location_has_cataclysm_dao.get_all_location_has_cataclysms()

    def get_location_has_cataclysm(self, id, location_id, cataclysm_id):
        return self.location_has_cataclysm_dao.get_location_has_cataclysm(id, location_id, cataclysm_id)

    def update_location_has_cataclysm(self, id, location_id, cataclysm_id, new_location_id, new_cataclysm_id):
        return self.location_has_cataclysm_dao.update_location_has_cataclysm(id, location_id, cataclysm_id, new_location_id, new_cataclysm_id)

    def delete_location_has_cataclysm(self, id, location_id, cataclysm_id):
        return self.location_has_cataclysm_dao.delete_location_has_cataclysm(id, location_id, cataclysm_id)