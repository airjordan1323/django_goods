from django.urls import path, include
from . import views

urlpatterns = [
    path("get-trans/", views.TransListView.as_view()),
    path("trans/", views.TransPostView.as_view()),
    path("buy/", views.BuyView.as_view()),
    path("buy-silk/", views.BuySilkView.as_view()),
]
