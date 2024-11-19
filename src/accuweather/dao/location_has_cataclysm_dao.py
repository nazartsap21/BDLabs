from src.accuweather.domain.models import LocationHasCataclysm


class LocationHasCataclysmDao:
    def __init__(self, session):
        self.session = session

    def create_location_has_cataclysm(self, location_id, cataclysm_id):
        new_location_has_cataclysm = LocationHasCataclysm(location_id=location_id, cataclysm_id=cataclysm_id)
        self.session.add(new_location_has_cataclysm)
        self.session.commit()
        return new_location_has_cataclysm

    def get_all_location_has_cataclysms(self):
        return self.session.query(LocationHasCataclysm).all()

    def get_location_has_cataclysm(self, id, location_id, cataclysm_id):
        return self.session.query(LocationHasCataclysm).get((id, location_id, cataclysm_id))

    def update_location_has_cataclysm(self, id, location_id, cataclysm_id, new_location_id, new_cataclysm_id):
        location_has_cataclysm = self.session.query(LocationHasCataclysm).get((id, location_id, cataclysm_id))
        if location_has_cataclysm:
            location_has_cataclysm.location_id = new_location_id
            location_has_cataclysm.cataclysm_id = new_cataclysm_id
            self.session.commit()
        return location_has_cataclysm

    def delete_location_has_cataclysm(self, id, location_id, cataclysm_id):
        location_has_cataclysm = self.session.query(LocationHasCataclysm).get((id, location_id, cataclysm_id))
        if location_has_cataclysm:
            self.session.delete(location_has_cataclysm)
            self.session.commit()
        return location_has_cataclysm
