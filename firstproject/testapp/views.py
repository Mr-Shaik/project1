from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def http_response_view(request):
    content = '<p>dummy content</p>'
    return HttpResponse(content)

