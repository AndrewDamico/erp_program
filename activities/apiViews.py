from django.core import serializers
from django.http import JsonResponse
from .models import Activity, Status
from budget_app.models import ProjectCharter
from a2dam.models import EventClass
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getProjects(request):
    project = ProjectCharter.objects.all()
    project_obj = serializers.serialize('python',project)
    return JsonResponse(project_obj, safe=False)

@csrf_exempt
def getStatus(request):
    status = Status.objects.all()
    status_obj = serializers.serialize('python',status)
    return JsonResponse(status_obj, safe=False)

@csrf_exempt
def getEventClass(request):
    eventclasses = EventClass.objects.all()
    class_obj = serializers.serialize('python',eventclasses)
    return JsonResponse(class_obj, safe=False)

@csrf_exempt
def ledit_activities(requests):

    id = requests.POST.get('id','')
    value = requests.POST.get('value','')
    activity = Activity.objects.get(id=id)
    type = requests.POST.get('type','')

    if type == "action":
        activity.action = value
    if type == "wbs":
        activity.wbs = value
    if type == "duration":
        activity.duration = value
    if type == "start_date":
        activity.start_date = value
    if type == "end_date":
        activity.end_date = value
    if type == "due_date":
        activity.due_date = value
    if type == "time":
        activity.time = value
    if type == "work":
        activity.work = value
    if type == "is_active":
        activity.is_active = value

    activity.save()

    return JsonResponse({"success":"Updated"})


