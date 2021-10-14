from django.urls import path
from .views import index, create
urlpatterns = [
    path('', index, name='publications'),
    path('index', index),
    path('create', create, name='create'),
]