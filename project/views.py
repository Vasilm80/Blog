from django.shortcuts import render


from project.models import myproject


# Create your views here.
def project_index(request):
    projects = myproject.objects.all()
    context = {'projects': projects}

    return render(request, 'projects_index.html', context)

def index(request):
    return render(request, 'index.html')

def project_detail(request, pk):
    projects = myproject.objects.get(pk = pk)
    context = {'project': projects}
    return render(request, 'project_detail.html', context)