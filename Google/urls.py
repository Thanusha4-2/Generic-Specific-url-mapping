from django.urls import path
from Google.views import *

urlpatterns=[
    path('CEO/',CEO,name='CEO'),
    path('Founder/',Founder,name='Founder'),
]