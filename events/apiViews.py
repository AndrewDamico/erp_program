from django.core import serializers
from django.http import JsonResponse
from .models import Event
from budget_app.models import ProjectCharter
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getProjects(request):
    project = ProjectCharter.objects.all()
    project_obj = serializers.serialize('python',project)

    return JsonResponse(project_obj, safe=False)

@csrf_exempt
def live_edit(requests):
    id = requests.POST.get('id','')
    value = requests.POST.get('value','')
    event = Event.objects.get(id=id)
    if type == "name":
        event.name = value
    if type == "project":
        event.project = value
    if type == "date":
        event.date = value
    if type == "description":
        event.description = value
    if type == "is_active":
        event.is_active = value
    event.save()
    return JsonResponse({"success":"Updated"})


