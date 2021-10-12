from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная БибоСтраница')

def posts(request, slug):
    return HttpResponse('Детали БибоСайта')