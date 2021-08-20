from django.shortcuts import render
from apps.portfolio.models import Projects

# Create your views here.
def projects(request):
    projects= Projects.objects.all()
    context={
        'projects':projects,
    }
    return render(request, 'projects.html', context)