from django.core import serializers
from django.http import JsonResponse

from budget_app.models import ProjectCharter
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getProjects(request):
    project = ProjectCharter.objects.all()
    project_obj = serializers.serialize('python',project)

    return JsonResponse(project_obj, safe=False)
