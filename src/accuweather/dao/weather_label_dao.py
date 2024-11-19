from src.accuweather.domain.models import WeatherLabel


class WeatherLabelDao:
    def __init__(self, session):
        self.session = session

    def create_weather_label(self, name, link):
        new_weather_label = WeatherLabel(name=name, link=link)
        self.session.add(new_weather_label)
        self.session.commit()
        return new_weather_label

    def get_all_weather_labels(self):
        return self.session.query(WeatherLabel).all()

    def get_weather_label(self, id):
        return self.session.query(WeatherLabel).get(id)

    def update_weather_label(self, id, name, link):
        weather_label = self.session.query(WeatherLabel).get(id)
        if weather_label:
            weather_label.name = name
            weather_label.link = link
            self.session.commit()
        return weather_label

    def delete_weather_label(self, id):
        weather_label = self.session.query(WeatherLabel).get(id)
        if weather_label:
            self.session.delete(weather_label)
            self.session.commit()
        return weather_label