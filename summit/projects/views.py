from django.shortcuts import render
from projects.models import Project

# Create your views here.


def project_index(request):
    projects = Project.objects.all

    return render(request, 'projects/project_index.html', { 'projects': projects })
