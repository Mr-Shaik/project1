import datetime

from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def date_time_view(requet):
    date=datetime.datetime.now()
    s='<h1> The current Date and Time at server is :' + str(date)
    return HttpResponse(s)