from django.utils import timezone
from django.conf import settings
from datetime import datetime
import requests

from django.shortcuts import render

from django.views import generic

from .models import WeatherForecast

class IndexView(generic.ListView):
    template_name = 'weather/index.html'
    context_object_name = 'forecast_list'

    def get_queryset(self):
        """
        Return the last five weather forecasts.
        """

        resp = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=13.892505&lon=-8.837564&appid=' + settings.OWM_API_KEY).json()
        forecast = WeatherForecast(

            date = datetime.now(),
            temperature = resp['main']['temp'],
            rainfall = 22.3,
            wind_speed = resp['wind']['speed']
        )
        return [forecast]

class WeatherView(generic.DetailView):
    model = WeatherForecast
    template_name = 'weather/forecast.html'
    context_object_name = 'forecast_day'
