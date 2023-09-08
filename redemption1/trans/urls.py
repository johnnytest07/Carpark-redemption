from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.home_page, name="home"),
    path('submit', views.submit, name='submit'),
]
