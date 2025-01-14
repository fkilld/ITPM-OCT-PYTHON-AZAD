from django.shortcuts import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse( 'about.html')


def prashant(request):
    return HttpResponse( 'prshant.html')