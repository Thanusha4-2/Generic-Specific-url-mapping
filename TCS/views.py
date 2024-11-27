from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def CEO(request):
    return HttpResponse('<h1>Krithivasan is the CEO of TCS</h1>')

def Founder(request):
    return HttpResponse('<h1>Faqir Chand Kohli and J.R.D Tata are founders of Google</h1>')

