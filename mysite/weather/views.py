from django.utils import timezone


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
        return WeatherForecast.objects.order_by('-date')[:5]

class WeatherView(generic.DetailView):
    model = WeatherForecast
    template_name = 'weather/forecast.html'
    context_object_name = 'forecast_day'
