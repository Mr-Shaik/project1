from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# def wish_view(request):
#         msg='raj'
# return render(request,'testapp/results.html',{'msg':msg})
def wish_view(request):
    msg="Bestlacloud"
    #return render(request,'templates/results.html',{'msg':msg})

    #return render(request, 'testapp/results.html', {'msg':msg})
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='Hello Guest !!! Very Good'
    if h<12:
        msg=msg+"Morning"
    elif h<16:
        msg=msg+"Afternoon"
    elif h<21:
        msg=msg+"Evening"
    else:
        msg=msg+"Night"
    response = render(request,'testapp/results.html',{'m':msg,'date':date})#,{'date':date})
    return  response;