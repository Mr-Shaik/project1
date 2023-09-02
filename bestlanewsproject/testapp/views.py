from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page_view(request):
    home="Hello welcome to home page"
    return render(request,'testapp/home.html'
                  ,{'home':home})
    # response = render(request,'testapp/results.html',{'m':msg,'date':date})#,{'date':date})
    # return  response;
def movie_news_view(request):
    news1="In Telugu DevDas Movie is not Good"
    news2="Salman updating minimum 100 cr0s Guarantee"
    news3="Sonali Slowly Getting Curing"
    news4="Amitabh Next movie is Thugs of Hindstan"
    news5="Pavan getting new things to "
    my_dict={"news1":news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'testapp/movienews.html',my_dict)