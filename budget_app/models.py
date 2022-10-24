from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

'''
class AccountInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_budget = models.IntegerField()
    
    def __str__(self):
        return self.username
'''

class Quarter(models.Model):
    quarter_name = models.CharField(max_length=20)
    def __str__(self):
        return self.quarter_name

class FiscalYear(models.Model):
    FY_name = models.CharField(max_length = 20)
    FY_start_date = models.DateField('FY Start Date')
    FY_end_date = models.DateField('FY End Date')
    def __str__(self):
        return self.FY_name

class Schedule(models.Model):
    schedule_name = models.CharField(max_length = 20, blank=True, null=True)
    event_date = models.DateField('Event Date', blank=True, null=True)
    start_date = models.DateField('Schedule Start Date', blank=True, null=True)
    end_date = models.DateField('Schedule End Date', blank=True, null=True)
    fiscalyear = models.ForeignKey(FiscalYear, on_delete=models.PROTECT)
    quarter = models.ForeignKey(Quarter, on_delete=models.PROTECT)
    @property
    def date(self):
        if self.event_date == None:
            return self.start_date
        else:
            return self.event_date
    def __str__(self):
        if not self.start_date:
            self.start_date = self.fiscalyear.FY_start_date
        if not self.end_date:
            self.end_date = self.fiscalyear.FY_end_date
        if not self.event_date:
            self.event_date = self.start_date
        if not self.schedule_name:
            self.schedule_name = f"{self.quarter} {self.fiscalyear} ({self.start_date} to {self.end_date})"
        return self.schedule_name
    # Approval

class ExpenseInfo(models.Model):
    Quarters = (
        ('Fall', 'Fall'),
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer')
    )
    event_name = models.CharField(max_length=20)
    expense_name = models.CharField(max_length=20)
    year = models.IntegerField()
    quarter = models.CharField(max_length=20,choices=Quarters)
    cost = models.FloatField()
    date_added = models.DateField()
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.event_name

class ScopeItem(models.Model):
    name = models.CharField(max_length=20)
    fixed_cost = models.IntegerField(blank=True, default=0, null=True)
    variable_cost = models.IntegerField(blank=True, default=0, null=True)
    description = models.TextField()
    # approval
    def __str__(self):
        return self.name

class ScopeStatement(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    size = models.IntegerField()
    items = models.ManyToManyField(ScopeItem)
    def __str__(self):
        if not self.description:
            self.description = self.name
        return self.description

class CostType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class BudgetItem(models.Model):
    cost_type = models.ForeignKey(CostType, on_delete=models.PROTECT)
    cost = models.IntegerField()
    def __str__(self):
        return f"{str(self.cost_type)}: ${self.cost}"

class Budget(models.Model):
    name = models.CharField(max_length=30)
    items = models.ManyToManyField(BudgetItem)
    #receipts
    #approval
    def __str__(self):
        return self.name
    def cost(self):
        return BudgetItems.objects.filter(Budget=self).aggregate(Sum("cost"))['cost__sum']

class ProjectCharter(models.Model):
    name = models.CharField(max_length=30)
    budget = models.ForeignKey(Budget, on_delete=models.PROTECT)
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    scope = models.ForeignKey(ScopeStatement, on_delete=models.PROTECT)
    sponsor = models.CharField(max_length=30)
    #approval
    @property
    def date(self):
        return self.schedule.date
    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=30)
    project = models.ManyToManyField(ProjectCharter)
    def __str__(self):
        return self.name
    def programcost(self):
        return Budget.objects.filter(Program=self).aggregate(Sum('cost'))['cost__sum']

class AnnualBudget(models.Model):
    program = models.ManyToManyField(Program)
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT)
    #approval

'''
class Budget(models.Model):
    budget_item = models.CharField(max_length=20)
    budget_quarter = models.CharField(max_length=20)
    class fiscal_year(models.IntegerChoices):
        2022
        2023
    fiscal_year = models.IntegerField(choices=fiscal_year.choices)
    cost = models.FloatField()
    date_added = models.DateField()
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)
'''