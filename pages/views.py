from django.shortcuts import render
from django.http import HttpResponse # create a response to a URL request 



# Create your views here.

def homePageView(request):
    ''' This function will respond to an HTTP request and return an HttpRequest object.'''

    return HttpResponse('Hello, world!')