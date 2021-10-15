from django.urls import path
from .views import *
urlpatterns = [
    path('sign_up/', register, name='register'),
    path('sign_in/', user_login, name='login'),
    path('sign_out/', user_logout, name='logout')
]