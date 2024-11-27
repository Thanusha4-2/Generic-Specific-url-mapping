"""
URL configuration for MNC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Wipro.views import *
from infosys.views import *
from django.urls import path,include
import Google,TCS


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Ravi/',Ravi,name='Ravi'),
    path('Swetha/',Swetha,name='Swetha'),
    path('Bangalore/',Bangalore,name='Bangalore'),
    path('Hyderabad/',Hyderabad,name='Hyderabad'),
    path('Google/',include('Google.urls')),
    path('TCS/',include('TCS.urls')), 
]
