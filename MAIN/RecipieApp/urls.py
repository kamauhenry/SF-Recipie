
from django.urls import path
from . import views
from .views import home, recipies, Recipie

urlpatterns = [
    path("", views.home),
    path('recipies/,<slug>/', recipies, name='recipies'),
    path('recipie/' ,Recipie, name='Recipie'),
    path('home/' ,home, name='home'),
]