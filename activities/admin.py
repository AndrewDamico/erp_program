from django.contrib import admin
from .models import *

models = [
    Activity,
    Relationship,
    Status,
    Predecesor
]

for model in models:
    admin.site.register(model)
