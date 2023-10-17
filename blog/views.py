from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post, Coments


# Create your views here.

def blog_index (request):
    posts = Post.objects.all().order_by('title')
    context = {
       'posts': posts,
    }
    return render(request, 'blog_index.html', context)

def blog_detail (request, pk):
    post = Post.objects.get(pk = pk)
    comments = Coments.objects.filter(post = post)
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog_detail.html', context)

def blog_category (request, category):
    posts = Post.objects.filter(categories__name__contains=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog_category.html', context)
# @csrf_exempt
# def index(request):
#     ss = request.POST['b']
#     print(ss)
#     return HttpResponse('POST запрос успешно обработан.')


