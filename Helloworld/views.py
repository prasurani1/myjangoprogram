from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('HI WELCOME TO MY NEW DJANGO APP,THIS IS A DEMO DJANGO PROGRAM!')

# Create your views here.
