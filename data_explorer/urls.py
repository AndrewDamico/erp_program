from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('data_explorer/', data_explorer, name='data_explorer'),
]

