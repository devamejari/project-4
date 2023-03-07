from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def deva(request):
    return  HttpResponse('<h1><marquee>jammalakadi jarmitay</h1></marquee>')