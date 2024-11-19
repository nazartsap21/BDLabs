from src.accuweather.domain.models import Cataclysm, Location, LocationHasCataclysm


class CataclysmDao:
    def __init__(self, session):
        self.session = session

    def create_cataclysm(self, title, description, start_date, end_date):
        new_cataclysm = Cataclysm(title=title, description=description, start_date=start_date, end_date=end_date)
        self.session.add(new_cataclysm)
        self.session.commit()
        return new_cataclysm

    def get_all_cataclysms(self):
        return self.session.query(Cataclysm).all()

    def get_cataclysm(self, id):
        return self.session.query(Cataclysm).get(id)

    def update_cataclysm(self, id, title, description, start_date, end_date):
        cataclysm = self.session.query(Cataclysm).get(id)
        if cataclysm:
            cataclysm.title = title
            cataclysm.description = description
            cataclysm.start_date = start_date
            cataclysm.end_date = end_date
            self.session.commit()
        return cataclysm

    def delete_cataclysm(self, id):
        cataclysm = self.session.query(Cataclysm).get(id)
        if cataclysm:
            self.session.delete(cataclysm)
            self.session.commit()
        return cataclysm

    def get_locations_by_cataclysm(self, id):
        return self.session.query(Location).join(LocationHasCataclysm, Location.id == LocationHasCataclysm.location_id).filter(LocationHasCataclysm.cataclysm_id == id).all()