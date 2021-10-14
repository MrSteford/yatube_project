from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = 'Это главная страница проекта Yatube'
    context = {
        'title' : title
    }
    template = 'posts/index.html'
    return render(request, template, context)

def posts(request, list):
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title' : title
    }
    template = 'posts/group_list.html'
    return render(request, template, context)