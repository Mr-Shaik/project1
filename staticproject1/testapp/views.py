import datetime

from django.shortcuts import render

# Create your views here.


def date_time_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    if h < 12:
        msg="Hello Guest very Good Morning"
    elif h < 16:
        msg="Hello Guest Very Good Afternoon"
    elif h < 21:
        msg="Hello Guset very Good Evening "
    else:
        msg="Hello Guest Good Night"
    my_dict={'date':date,'msg':msg}
    #return render(result,'testapp/results.html',my_dict)
    #return render(result,'testapp/html/',my_dict)
    # response = render(request, 'testapp/results.html', {'m': msg, 'date': date})  # ,{'date':date})
    # return response;
    response = render(request,'testapp/results.html',my_dict)
    return response;

