
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('',include('myapp1.urls')),
path('about/',include('myapp2.urls')),
    
]
