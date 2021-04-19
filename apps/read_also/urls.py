from django.urls import path
from . import views

urlpatterns = [
    path("news-list/", views.NewsListView.as_view()),
    path("news-lt/", views.NewsListTwoView.as_view()),
    path("news-det/<int:pk>/", views.NewsDetailView.as_view()),
]