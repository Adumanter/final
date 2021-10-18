from django.urls import path
from .views import index, create
urlpatterns = [
    path('', index, name='crafts'),
    path('create_craft', create, name='create_craft'),

]