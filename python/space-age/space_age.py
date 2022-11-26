class SpaceAge:

    year_seconds_on_earth = 31557600
    year_by_earth = {
        "earth": 1,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }

    def __init__(self, seconds):
        self.year_on_earth = seconds / self.year_seconds_on_earth

    def on_earth(self):
        return round(self.year_on_earth, 2)

    def on_mercury(self):
        return round(self.year_on_earth / self.year_by_earth["mercury"], 2)

    def on_venus(self):
        return round(self.year_on_earth / self.year_by_earth["venus"], 2)

    def on_mars(self):
        return round(self.year_on_earth / self.year_by_earth["mars"], 2)

    def on_jupiter(self):
        return round(self.year_on_earth / self.year_by_earth["jupiter"], 2)

    def on_saturn(self):
        return round(self.year_on_earth / self.year_by_earth["saturn"], 2)

    def on_uranus(self):
        return round(self.year_on_earth / self.year_by_earth["uranus"], 2)

    def on_neptune(self):
        return round(self.year_on_earth / self.year_by_earth["neptune"], 2)
