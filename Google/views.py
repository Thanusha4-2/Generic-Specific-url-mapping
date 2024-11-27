from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def CEO(request):
    return HttpResponse('<h1>Sundhar Pichai is the CEO of Google</h1>')

def Founder(request):
    return HttpResponse('<h1>Larry Page and Sergey Brin are founders of Google</h1>')