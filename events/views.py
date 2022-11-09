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

def read_all(request):
    try:
        venues = Venue.objects.all()
        events = Event.objects.all()
           #venue.save()
        messages.success(request, "Successful")
    except:
        messages.error(request, "Failed")

    context = {
            'venues':venues,
            'events':events
        }

    return render(request,"events.html", context)

def delete_event(request, event_id):
    return HttpResponse("Event ID")

def delete_venue(request, venue_id):
    return HttpResponse("Event ID")

# EVENT MANAGEMENT
def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if event == None:
        return HttpResponse("Event not found")
    else:
        return render(request,"event_edit.html",{'event':event})

def edit_event(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        event = Event.objects.get(id=request.POST.get('id'))
        if event == None:
            return HttpResponse("<h2>Event Not Found</h2>")
        else:
            event.name = request.POST.get('name','')
            event.description = request.POST.get('description','')
            event.date = request.POST.get('date','')
            event.is_active = request.POST.get('is_active','')
            event.save()
            messages.success(request, "Successful")

        return HttpResponseRedirect("update_event/"+str(event.id)+"")

# LOCATION MANAGEMENT
def update_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    if venue == None:
        return HttpResponse("Venue not found")
    else:
        return render(request, "venue_edit.html",{'venue':venue})


def edit_venue(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        venue = Venue.objects.get(id=request.POST.get('id'))
        if venue == None:
            return HttpResponse("<h2>Venue Not Found</h2>")
        else:
            venue.name = request.POST.get('name','')
            venue.type = request.POST.get('type','')
            venue.is_active = request.POST.get('is_active','')
            venue.save()
            messages.success(request, "Successful")

        return HttpResponseRedirect("update_venue/"+str(venue.id)+"")