from django.urls import path
from .views import index, contact, about
urlpatterns = [
    path('', index),
    path('index', index),
    path('contact', contact),
    path('about', about)
]