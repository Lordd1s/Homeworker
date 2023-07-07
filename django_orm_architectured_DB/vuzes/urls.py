from django.urls import path
from vuzes import views

urlpatterns = [
    path('', views.home, name="home"),
]