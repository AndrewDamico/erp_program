from django.urls import path,include
from . import views, apiViews
from django.contrib.auth import views as auth_views
from .views import *
from .apiViews import *


urlpatterns = [

    path('activities', views.activity_list, name="Activities"),
    path('addActivity', views.addActivity, name="Add Activity"),
    path('add_activity', views.add_activity, name="add_Event"),
    path('edit_activity',views.edit_activity,name="edit_activity"),
    path('update_activity/<str:activity_id>',views.update_activity,name="update_activity"),
    path('delete_activity/<str:activity_id>',views.delete_activity,name="delete_activity"),

    # Get select dropdown values
    path(
        'get_projects',
        apiViews.getProjects,
        name="get_projects"),

    path(
        'get_status',
        apiViews.getStatus,
        name="get_status"),

    path(
        'get_eventclass',
        apiViews.getEventClass,
        name="get_eventclass"),

    path(
        'ledit_activities',
        apiViews.ledit_activities,
        name="ledit_activities"),
]
