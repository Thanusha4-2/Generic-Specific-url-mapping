from django.urls import path
from TCS.views import *

urlpatterns=[
    path('CEO/',CEO,name='CEO'),
    path('Founder/',Founder,name='Founder'),
]