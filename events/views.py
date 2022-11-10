from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from budget_app.models import ProjectCharter

# Create your views here.
def addEvent(request):
    projects = ProjectCharter.objects.all()
    context = {
        "projects":projects
    }
    return render(request,"add_event.html", context)

def events(request):
    context = {
    'k1': 'Welcome to the Events page',
    }
    return render(request, 'events.html', context)


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


# EVENT MANAGEMENT
def add_event(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        charter_id = request.POST.get('project')
        instance = ProjectCharter.objects.filter(id=charter_id)[0]
        event = Event(
            name = request.POST.get('name',''),
            project = instance,
            description = request.POST.get('description',''),
            date = request.POST.get('date',''),
            start_time = request.POST.get('start_time',''),
            end_time = request.POST.get('end_time','')
        )
        event.save()
        messages.success(request, "Successful")

            #messages.error(request, "Failed")
        return HttpResponseRedirect('read_all')

def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    projects = ProjectCharter.objects.all
    if event == None:
        return HttpResponse("Event not found")
    else:
        return render(request,"event_edit.html",{'event':event,'projects':projects})

def edit_event(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        event = Event.objects.get(id=request.POST.get('id'))
        if event == None:
            return HttpResponse("<h2>Event Not Found</h2>")
        else:
            project_id = request.POST.get('project','')
            instance = ProjectCharter.objects.filter(id=project_id)[0]
            event.name = request.POST.get('name','')
            event.description = request.POST.get('description','')
            event.project = instance
            event.date = request.POST.get('date','')
            event.is_active = request.POST.get('is_active','')
            event.save()
            messages.success(request, "Successful")

        return HttpResponseRedirect('read_all')
        #return HttpResponseRedirect("update_event/"+str(event.id)+"")

def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    messages.error(request, "Sucessfull Deletion")

    return HttpResponseRedirect('/read_all')

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

        return HttpResponseRedirect('read_all')
        #return HttpResponseRedirect("update_venue/"+str(venue.id)+"")

def delete_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    venue.delete()
    messages.error(request, "Sucessfull Deletion")

    return HttpResponseRedirect('/read_all')