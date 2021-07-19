from django.http.response import HttpResponse
from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)


def index2(request):
    return HttpResponse("hi helloo!")