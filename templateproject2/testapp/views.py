import datetime

from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.


def template_view(request):
    #HttpResponse s= render(request,'testapp/result.html')
    #return s
    #or
    dt=datetime.datetime.now();
    #my_dict={'date':dt}
   # return render(request,'testapp/result.html',context=my_dict);
    #return render(request, 'testapp/result.html',my_dict);

#    return render(request, 'testapp/result.html',{'date':dt});
    name='BestlaCloud'
    rollno=1001
    marks=90
    my_dict={'date':dt,'name':name,'rollno':rollno,'marks':marks}


    return render(request, 'testapp/result.html', my_dict);
