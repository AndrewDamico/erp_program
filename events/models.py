from django.db import models
from datetime import datetime
from django.utils.dateformat import DateFormat, TimeFormat
from django.utils import timezone
from budget_app.models import ProjectCharter
from a2dam.models import EventClass
from activities.models import Status
from polymorphic.models import PolymorphicModel

# Create your models here.

class agenda_item(PolymorphicModel):
    subject = models.CharField(max_length=512)
    body = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Event(agenda_item):
    # Class Properties
    #subject = models.CharField(max_length=255)
    #body = models.TextField(null=True, blank=True)
    #start_time = models.DateTimeField(default=timezone.now())
    #end_time = models.DateTimeField(default=timezone.now())

    #ERP Properties
    #id = models.AutoField(primary_key=True)
    project = models.ForeignKey(ProjectCharter, on_delete=models.CASCADE)
    eventclass = models.ForeignKey(EventClass, on_delete=models.CASCADE)
    #date = models.DateField() #Deleted
    #META
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    Default = datetime.today().strftime("mm/dd/yyyy")

    #TODO
    #@property
    #def start_time(self):
    #    return TimeFormat(self.start_time).format("H:i")
    #@property
    #def startdate():
    #    return (Default.strftime("%Y-%m-%d"))

    def __str__(self):
        return self.name
    def date_format(self):
        df = DateFormat(self.date)
        return df.format("Y-m-d")

#class OutlookEvents(Event):


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
