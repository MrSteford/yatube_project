from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 
    # title = 'Это главная страница проекта Yatube'
    # context = {
    #     'title' : title
    # }
    # template = 'posts/index.html'
    #return render(request, template, context)

def posts(request, slug):
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title' : title
    }
    template = 'posts/group_list.html'
    return render(request, template, context)