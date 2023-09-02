from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def  first_view(response):
    return  HttpResponse('<h1> Response from First View</h1>')

def  second_view(response):
    return  HttpResponse('<h1> Response from second View</h1>')

def  third_view(response):
    return  HttpResponse('<h1> Response from third View</h1>')

def  fourth_view(response):
    return  HttpResponse('<h1> Response from Fourth View</h1>')

def  fifth_view(response):
    return  HttpResponse('<h1> Response from Fifth View</h1>')
