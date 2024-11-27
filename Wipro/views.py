from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Ravi(request):
    return HttpResponse('<h1>Ravi is a project manager</h1>')

def Swetha(request):
    return HttpResponse('<h1>Swetha is a Software Developer</h1>')