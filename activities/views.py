from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from budget_app.models import ProjectCharter
from activities.models import Activity
from a2dam.models import EventClass



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

def addActivity(request):
    projects = ProjectCharter.objects.all()
    status = Status.objects.all()
    eventclasses = EventClass.objects.all()
    context = {
        "projects":projects,
        "status":status,
        "eventclasses":eventclasses
    }
    return render(request, "add_activity.html", context)


# EVENT MANAGEMENT
def add_activity(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        charter_id = request.POST.get('project')
        status_id = request.POST.get('status')
        eventclass_id = request.POST.get('eventclass')

        project_inst = ProjectCharter.objects.filter(id=charter_id)[0]
        eventclass_inst = EventClass.objects.filter(id=eventclass_id)[0]
        status_inst = Status.objects.filter(id=status_id)[0]

        activity=Activity(
            eventclass = eventclass_inst,
            action = request.POST.get('action',''),
            wbs = request.POST.get('wbs',''),
            description=request.POST.get('description',''),
            project = project_inst,
            duration = request.POST.get('duration',''),
            start_date = request.POST.get('start_date',''),
            end_date = request.POST.get('end_date',''),
            due_date = request.POST.get('due_date',''),
            time = request.POST.get('time',''),
            work = request.POST.get('work',''),
            status = status_inst,
            #predecessor = request.POST.get('predecessor',''),
            is_active = request.POST.get('is_active','')
        )
        activity.save()
        messages.success(request, "Successful")
            #messages.error(request, "Failed")
        return HttpResponseRedirect('activities')

def update_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    projects = ProjectCharter.objects.all
    status = Status.objects.all
    eventclass = EventClass.objects.all
    if activity == None:
        return HttpResponse("Event not found")
    else:

        context = {
            'activity':activity,
            'projects':projects,
            'status':status,
            'eventclass':eventclass
        }

        return render(request,"activity_edit.html",context)

def edit_activity(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        activity = Activity.objects.get(id=request.POST.get('id'))

        if activity == None:
            return HttpResponse("<h2>Activity Not Found</h2>")
        else:
            charter_id = request.POST.get('project')
            status_id = request.POST.get('status')
            eventclass_id = request.POST.get('eventclass')

            project_inst = ProjectCharter.objects.filter(id=charter_id)[0]
            eventclass_inst = EventClass.objects.filter(id=eventclass_id)[0]
            status_inst = Status.objects.filter(id=status_id)[0]

            activity.eventclass = eventclass_inst
            activity.project = project_inst
            activity.status = status_inst
            activity.description=request.POST.get('description','')
            activity.action=request.POST.get('action', '')
            activity.wbs=request.POST.get('wbs', '')

            activity.duration=request.POST.get('duration', '')
            activity.start_date=request.POST.get('start_date', '')
            activity.end_date=request.POST.get('end_date', '')
            activity.due_date=request.POST.get('due_date', '')
            activity.time=request.POST.get('time', '')
            activity.work=request.POST.get('work', '')

            # predecessor = request.POST.get('predecessor',''),
            activity.is_active=request.POST.get('is_active', '')

            activity.save()
            messages.success(request, "Successful")

        return HttpResponseRedirect('activities')
        #return HttpResponseRedirect("update_event/"+str(event.id)+"")

def delete_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    activity.delete()
    messages.error(request, "Activity Deleted.")

    return HttpResponseRedirect('activities')
