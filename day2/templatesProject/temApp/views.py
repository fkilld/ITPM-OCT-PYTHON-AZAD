from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'temApp/home.html')

def about(request):
    return render(request, 'about.html')

def idk(request):
    return render(request, 'idk.html')