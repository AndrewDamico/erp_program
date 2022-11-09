from django.db import models
from django.utils.dateformat import DateFormat

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    def __str__(self):
        return self.name
    def date_format(self):
        df = DateFormat(self.date)
        return df.format("Y-m-d")

class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    def __str__(self):
        return self.name
