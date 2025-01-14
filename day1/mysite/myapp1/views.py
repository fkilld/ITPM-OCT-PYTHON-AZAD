from django.shortcuts import HttpResponse

# Create your views here.
def myapp1(request):
    return HttpResponse("Hello, world. You're at the myapp1 index.")


def home(request):
    return HttpResponse("Hello, world. You're at the home index.")

def server(request):
    return HttpResponse("Hello, world. You're at the server index.")


def Four0Four(request):
    return HttpResponse("<a href='/'>home </a>", status=404)