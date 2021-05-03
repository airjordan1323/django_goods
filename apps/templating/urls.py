from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news'),
    path('movies/', views.MovieListView.as_view(), name='movies'),
    path('media/', views.MediaListView.as_view(), name='media'),
    path('locations/', views.LocationView.as_view(), name='locations'),
    path('history/', views.HistoryView.as_view(), name='history'),
    path('press/', views.DayView.as_view(), name='press'),
    path('', views.GuestsAndPartnersView.as_view(), name='index'),
    path('kino/', views.kino, name='kino'),
]
