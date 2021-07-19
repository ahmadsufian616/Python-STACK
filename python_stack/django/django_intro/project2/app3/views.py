from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def i(request):
    return HttpResponse("hi my first djanfgo project app3")

def i2(request):
    return HttpResponse("hi helloo! app32") 