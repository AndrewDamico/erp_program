from django.db import models
from events.models import agenda_item
from django.utils import timezone


class OutlookEvent(models.Model):
    # Class Properties
    subject = models.CharField(max_length=512)
    body = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    #Outlook Properties
    id = models.CharField(primary_key=True, max_length=256)
    change_key = models.CharField(max_length=128)
    organizer = models.CharField(max_length=128)
    # all_day = "all_day"
    show_as = models.CharField(max_length=16)
