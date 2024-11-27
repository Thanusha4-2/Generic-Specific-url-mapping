from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Bangalore(request):
    return HttpResponse('<h1>There are 1 lakh infosys Employees in Bangalore')

def Hyderabad(request):
    return HttpResponse('<h1>There are 1 lakh infosys Employees in Hyderbad')