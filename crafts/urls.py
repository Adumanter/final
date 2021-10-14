from django.urls import path
from .views import index, create
urlpatterns = [
    path('', index, name='crafts'),
    path('create', create, name='create_craft'),

]