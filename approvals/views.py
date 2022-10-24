from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
import matplotlib.pyplot as plt
import numpy as np
import datetime
from django.db.models import Q


# Create your views here.
def approvals(request):
    context = {
        'k1': 'Welcome to the Second page',
    }
    return render(request, 'approvals.html', context)
