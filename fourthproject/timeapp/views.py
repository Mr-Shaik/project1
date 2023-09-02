import datetime

from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def time_info_view(request):
    time=datetime.datetime.now()
    s='<h1> Hello current Date and Time is :' +str(time)
    return HttpResponse(s)
