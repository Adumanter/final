from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('index1', index),
    path('contact', contact),
    path('about', about),
    path('publications/<int:aid>/', get_article, name='article'),
    path('turnir/<int:pk>/', get_turnir, name='get_turnir'),
    path('craft/<int:cid>/', get_craft, name='get_craft'),
    path('fish_news/<int:nid>/', get_news, name='single_fish_news'),

]