from typing import ContextManager
from django.http import request
from django.shortcuts import render,redirect


# Create your views here.
def fun(request):
    if 'visitcount' not in  request.session:
        request.session['visitcount']=1
      
    request.session['visitcount']+=1
        
    return render(request,"index.html")

def fun2(request):
    request.session['visitcount']=0
       

    return redirect("/")
