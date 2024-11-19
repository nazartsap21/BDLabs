from src.accuweather.dao.weather_label_dao import WeatherLabelDao


class WeatherLabelService:
    def __init__(self, weather_label_dao: WeatherLabelDao):
        self.weather_label_dao = weather_label_dao

    def create_weather_label(self, name: str, link: str):
        """Create a new weather label."""
        return self.weather_label_dao.create_weather_label(name, link)

    def get_all_weather_labels(self):
        """Retrieve all weather labels."""
        return self.weather_label_dao.get_all_weather_labels()

    def get_weather_label(self, id: int):
        """Retrieve a weather label by ID."""
        return self.weather_label_dao.get_weather_label(id)

    def update_weather_label(self, id: int, name: str, link: str):
        """Update a weather label's details."""
        return self.weather_label_dao.update_weather_label(id, name, link)

    def delete_weather_label(self, id: int):
        """Delete a weather label by ID."""
        return self.weather_label_dao.delete_weather_label(id)