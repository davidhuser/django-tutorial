from django.db import models



class WeatherForecast(models.Model):
    date = models.DateField('forecast day')
    temperature = models.FloatField()
    rainfall = models.FloatField()
    wind_speed = models.FloatField()

    def is_storm(self):
        return self.wind_speed >= 21.7