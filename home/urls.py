from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('contact', contact),
    path('about', about),
    path('publications/<int:aid>/', get_article, name='article')
]