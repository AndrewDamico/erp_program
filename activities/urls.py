from django.urls import path,include
from . import views, apiViews
from django.contrib.auth import views as auth_views
from .views import *
from .apiViews import *


urlpatterns = [

    path('activities/', views.activity_list, name="Activities")
]