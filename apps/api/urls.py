from django.urls import path
from . import views

urlpatterns = [
    path("weather/", views.WeatherCast.as_view())
]