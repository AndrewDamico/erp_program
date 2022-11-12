from django.db import models

import datetime
from django.utils.dateformat import DateFormat, TimeFormat
from budget_app.models import ProjectCharter
from a2dam.models import EventClass


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.value

class Relationship(models.Model):

    def __init__(self):
        self._SS = ("Start-Start", "SS")
        self._SF = ("Start-Finish", "SF")
        self._FS = ("Finish-Start", "FS")
        self._FF = ("Finish-Finish", "FF")

    @property
    def SS(self):
        return self._SS

    @property
    def SF(self):
        return self._SF

    @property
    def FS(self):
        return self._FS
    @property
    def FF(self):
        return self._FF

    def main(self):
        main = [self._SS, self._SF, self._FS, self._FF]
        return main



class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    eventclass = models.ForeignKey(EventClass, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    #level = {"1": models.IntegerField(),"2": models.IntegerField(),"3": models.IntegerField(),"4": models.IntegerField(),"level": models.IntegerField()}
    wbs = models.CharField(max_length=255)
    project = models.ForeignKey(ProjectCharter, on_delete=models.CASCADE)
    duration = models.CharField(max_length=255)
    #
    start_date = models.DateField()
    sch_start_date = models.DateTimeField(blank=True, null=True)
    #
    end_date = models.DateField()
    sch_end_Date = models.DateTimeField(blank=True, null=True)
    #
    sch_duration = models.DurationField(blank=True, null=True)
    due_date = models.DateField()
    sch_due_date = models.DateTimeField(blank=True, null=True)
    time = models.DecimalField(max_digits=19, decimal_places=3, default=0)
    work = models.DecimalField(max_digits=19, decimal_places=10, default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    predecessor = models.ManyToManyField('Predecesor', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    # TODO user
    def __str__(self):
        return self.activity


class Predecesor(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.DecimalField(max_digits=19, decimal_places=15, default=0)
    name = models.ManyToManyField(Activity,blank=False, null=True)
    type = models.CharField(
        max_length=2,
    )