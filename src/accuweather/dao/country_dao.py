from src.accuweather.domain.models import Country, City


class CountryDao:
    def __init__(self, session):
        self.session = session

    def create_country(self, name, continent):
        new_country = Country(name=name, continent=continent)
        self.session.add(new_country)
        self.session.commit()
        return new_country

    def get_all_countries(self):
        return self.session.query(Country).all()

    def get_country(self, id):
        return self.session.query(Country).get(id)

    def update_country(self, id, name, continent):
        country = self.session.query(Country).get(id)
        if country:
            country.name = name
            country.continent = continent
            self.session.commit()
        return country

    def delete_country(self, id):
        country = self.session.query(Country).get(id)
        if country:
            self.session.delete(country)
            self.session.commit()
        return country

    def get_cities_by_country(self, id):
        return self.session.query(City).filter_by(country_id=id).all()