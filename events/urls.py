from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [

    path('events', events, name="Events"),
    path('addEvent', views.addEvent, name="Add Event"),
    path('add_event', views.add_event, name="add_Event"),
    path('add_venue', views.add_venue, name="add_Venue"),
    path('read_all', views.read_all, name="read_all"),
    path(
        'edit_venue',
        views.edit_venue,
        name="edit_venue"),
    path(
        'update_venue/<str:venue_id>',
        views.update_venue,
        name = "update_venue"),
    path(
        'delete_venue/<str:venue_id>',
        views.delete_venue,
        name="delete_venue"),
    path(
        'edit_event',
        views.edit_event,
        name="edit_event"),
    path(
        'update_event/<str:event_id>',
        views.update_event,
        name="update_event"),
    path(
        'delete_event/<str:event_id>',
        views.delete_event,
        name="delete_event"),
]

