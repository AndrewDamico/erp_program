from django.contrib import admin
from .models import *

models = [
    Event,
    Venue,
    EventProject
]

for model in models:
    admin.site.register(model)


from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
