from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForms
from blog.models import Post, Coments, UserModel


# Create your views here.

def blog_index (request):
    posts = Post.objects.all().order_by('title')
    context = {
       'posts': posts,
    }
    return render(request, 'blog_index.html', context)

def blog_detail (request, pk):
    post = Post.objects.get(pk = pk)
    form = CommentForms()
    if request.method == "POST":
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = Coments(
                autor=form.cleaned_data['autor'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    comments = Coments.objects.filter(post = post)
    context = {
        'post': post,
        'comments': comments,
        'form': form
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





