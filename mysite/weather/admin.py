from django.contrib import admin

from .models import WeatherForecast



class ForecastAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['temperature', 'wind_speed', 'rainfall']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]

    list_display = ('date', 'temperature', 'wind_speed', 'rainfall')
    list_filter = ['date']

admin.site.register(WeatherForecast, ForecastAdmin)