from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
import matplotlib.pyplot as plt
import numpy as np
from django.db.models import Q
# Create your views here.

def index(request):
    expense_items = ExpenseInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    try:
        budget_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(budget=Sum('cost',filter=Q(cost__gt=0)))
        expense_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(expenses=Sum('cost',filter=Q(cost__lt=0)))
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
    project_items = ProjectCharter.objects.all()
    context = {
        'project_items':project_items,
    }
    return render(request,'budget_app/projects.html', context=context)

def projects(request):
    project_items = ProjectCharter.objects.all()
    context = {
        'project_items':project_items,
    }
    return render(request,'budget_app/projects.html', context=context)

def table(request):
    expense_items = ExpenseInfo.objects.filter(user_expense=request.user).order_by('-date_added')
    try:
        budget_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(budget=Sum('cost',filter=Q(cost__gt=0)))
        expense_total = ExpenseInfo.objects.filter(user_expense=request.user).aggregate(expenses=Sum('cost',filter=Q(cost__lt=0)))
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

#DataFlair #Views #TemplateInheritance
# Create your views here.
def home(request):
    return render(request, 'base.html')
def other(request):
    context = {
    'k1': 'Welcome to the Second page',
    }
    return render(request, 'others.html', context)

import datetime
def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html',{'time': time})
