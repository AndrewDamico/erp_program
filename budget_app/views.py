from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
import matplotlib.pyplot as plt
import numpy as np
import datetime
from django.db.models import Q
# Create your views here.
'''
use a2dam_erp
select budget_app_projectcharter.name, budget_app_program.name, budget_app_program_project.program_id, budget_app_program_project.projectcharter_id
from budget_app_program, budget_app_projectcharter, budget_app_program_project
where budget_app_projectcharter.id = budget_app_program_project.projectcharter_id
AND budget_app_program.id = budget_app_program_project.program_id
'''

def index(request):
    expense_items = BudgetItem.objects.all()
    try:
        budget_total = BudgetItem.objects.all().aggregate(budget=Sum('cost',filter=Q(cost__gt=0)))
        expense_total = BudgetItem.objects.all().aggregate(expenses=Sum('cost',filter=Q(cost__lt=0)))
        fig,ax=plt.subplots()
        ax.bar(['Expenses','Budget'], [abs(expense_total['expenses']),budget_total['budget']],color=['red','green'])
        ax.set_title('Your total expenses vs total budget')
        plt.savefig('budget_app/static/budget_app/expense.jpg')
    except TypeError:
        print ('No data.')
    try:
        context = {'expense_items':expense_items,
                   'budget':budget_total['budget'],
                   'expenses':abs(expense_total['expenses']),
                   'remain':budget_total['budget']-abs(expense_total['expenses'])}
    except:
        context = {'expense_items': expense_items,
                   'budget': budget_total['budget'],
                   'expenses': abs(0),
                   'remain': budget_total['budget']-0,
                   }
    return render(request,'budget_app/index.html',context=context)


def programs(request):
    program_items = Program.objects.all()
    context = {
        'program_items':program_items,
    }
    return render(request,'budget_app/programs.html', context=context)

def projects(request):
    #Filtering
    if request.GET.get('featured'):
        featured_filter = request.GET.get('featured')
        project_items = ProjectCharter.objects.filter(featured_choices=featured_filter)
    else:
        project_items = ProjectCharter.objects.all()

    project_items = ProjectCharter.objects.all()
    context = {
        'project_items':project_items,
    }
    return render(request,'budget_app/projects.html', context=context)


def table(request):
    expense_items = BudgetItem.objects.all()
    try:
        budget_total = BudgetItem.objects.all().aggregate(budget=Sum('cost',filter=Q(cost__gt=0)))
        expense_total = BudgetItem.objects.all().aggregate(expenses=Sum('cost',filter=Q(cost__lt=0)))
        fig,ax=plt.subplots()
        ax.bar(['Expenses','Budget'], [abs(expense_total['expenses']),budget_total['budget']],color=['red','green'])
        ax.set_title('Your total expenses vs total budget')
        plt.savefig('budget_app/static/budget_app/expense.jpg')
    except TypeError:
        print ('No data.')
    try:
        context = {'expense_items':expense_items,
                   'budget':budget_total['budget'],
                   'expenses':abs(expense_total['expenses']),
                   'remain':budget_total['budget']-abs(expense_total['expenses'])}
    except:
        context = {'expense_items': expense_items,
                   'budget': budget_total['budget'],
                   'expenses': abs(0),
                   'remain': budget_total['budget']-0,
                   }
    return render(request,'budget_app/table.html',context=context)


def add_item(request):
    event_name = request.POST['event_name']
    name = request.POST['expense_name']
    year = request.POST['year']
    quarter = request.POST['quarter']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    ExpenseInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user, year=year, quarter=quarter)
    budget_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(budget=Sum('cost',filter=Q(cost__gt=0)))
    expense_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(expenses=Sum('cost',filter=Q(cost__lt=0)))
    fig,ax=plt.subplots()
    if expense_total['expenses'] == None:
        ax.bar(['Expenses','Budget'], [abs(0),budget_total['budget']],color=['red','green'])
    else:
        ax.bar(['Expenses', 'Budget'], [abs(expense_total['expenses']), budget_total['budget']], color=['red', 'green'])
    ax.set_title('Your total expenses vs. total budget')
    plt.savefig('budget_app/static/budget_app/expense.jpg')
    return HttpResponseRedirect('app')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return HttpResponseRedirect('app')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    else:
        form = UserCreationForm
        return render(request,'budget_app/sign_up.html',{'form':form})


def home(request):
    return render(request, 'base.html')

def other(request):
    context = {
    'k1': 'Welcome to the Second page',
    }
    return render(request, 'others.html', context)

def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html',{'time': time})

def gantt(request, template_name='gantt.htm'):
    # TODO get event start, end, and milestone from schedule
    if request.GET.get('sponsor_filter'):
        sponsor_filter = request.GET.get('sponsor_filter')
        project_items = ProjectCharter.objects.filter(sponsor=sponsor_filter)
    else:
        project_items = ProjectCharter.objects.all()
   #Implement zoom on the Gantt Chart
    if request.GET.get('zoom_level'):
       outlook_filter = request.GET.get('zoom_level')
    else:
        outlook_filter = 1
    quarters = Quarter.objects.all()
    context = {
        'project_items':project_items,
        'quarters':quarters,
        'outlook':outlook_filter
    }
    return render(request, template_name, context=context)

