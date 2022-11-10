from django.db import models
from django.utils.dateformat import DateFormat, TimeFormat
from budget_app.models import ProjectCharter

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    project = models.ForeignKey(ProjectCharter, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()

    #TODO
    #@property
    #def start_time(self):
    #    return TimeFormat(self.start_time).format("H:i")

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

class EventProject(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    project_id = models.ForeignKey(ProjectCharter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
