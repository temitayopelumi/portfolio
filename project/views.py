from django.shortcuts import render

# Create your views here.
from project.models import Project
def home(request):
    return render(request, 'project/base.html')
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project/project_detail.html', context)