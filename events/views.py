from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def addEvent(request):
    return render(request,"add_event.html")


def events(request):
    context = {
    'k1': 'Welcome to the Events page',
    }
    return render(request, 'events.html', context)

def add_event(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        try:
            event = Event(
                name = request.POST.get('name',''),
                description = request.POST.get('description',''),
                date = request.POST.get('date','')
            )
            event.save()
            messages.success(request, "Successful")
        except:
            messages.error(request, "Failed")
        return HttpResponseRedirect("/addEvent")

def add_venue(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        try:
            venue = Venue(
                name = request.POST.get('name', ''),
                type = request.POST.get('type', '')
            )
            venue.save()
            messages.success(request, "Successful")
        except:
            messages.error(request, "Failed")
        return HttpResponseRedirect("/addEvent")