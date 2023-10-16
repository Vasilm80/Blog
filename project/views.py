from django.shortcuts import render


from project.models import myproject


# Create your views here.
def project_index(request):
    projects = myproject.objects.all()
    name_pro = []
    for i in projects:
        name_pro.append(i.name)

    return render(request, 'projects_index.html', {'name': f'{name_pro}'})

def index(request):
    return render(request, 'index.html')

def project_detail(request, pk):
    proj = myproject.objects.get(pk = pk)
    dict_projects = {'Project': proj}
    return render(request, 'project_detail.html', dict_projects)