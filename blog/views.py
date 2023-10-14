from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def blog_index (request):
    return render(request, 'blog_index.html')

@csrf_exempt
def index(request):
    ss = request.POST['b']
    print(ss)
    return HttpResponse('POST запрос успешно обработан.')


