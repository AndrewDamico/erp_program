from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [

    path('events', events, name="Events"),
    path('addEvent', views.addEvent, name="Add Event"),
    path('add_event', views.add_event, name="add_Event"),
    path('add_venue', views.add_venue, name="add_Venue"),
]

