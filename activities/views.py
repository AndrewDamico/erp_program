from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from budget_app.models import ProjectCharter
from activities.models import Activity



def activity_list(request):
    try:
        activities = Activity.objects.all()
        messages.success(request, "Successful")
    except:
        messages.error(request, "Failed")

    context = {
            'activities':activities
        }

    return render(request,"activities.html", context)
