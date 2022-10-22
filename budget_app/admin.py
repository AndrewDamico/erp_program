from django.contrib import admin
from .models import *

models = [
    ExpenseInfo,
    Quarter,
    FiscalYear,
    Schedule,
    ScopeItem,
    ScopeStatement,
    BudgetItem,
    Budget,
    CostType,
    ProjectCharter,
    Program,
    AnnualBudget
]

for model in models:
    admin.site.register(model)


from django.contrib import admin

# Register your models here.
