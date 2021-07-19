from django.contrib.messages.api import error
from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def reg(request):
    error=User.objects.v(request.POST)
    if len(error) > 0 :
        for key, value in error.items():
            messages.error(request, value)
        return redirect("/")
            
    if request.POST['pass']!=request.POST['cpass']:
        return redirect("/")
    else:
        request.session['email']=request.POST['email']
        User.objects.create(first_name=request.POST['first'],last_name=request.POST['last'],email=request.POST['email'],password=request.POST['pass'])
        return redirect("/success")

def success(request):
    context={
        "email":request.session['email']
    }
    return render(request,"success.html",context)

def logout(request):
    del request.session['email']
    return redirect("/")

def log(request):
    user = User.objects.filter(email=request.POST['Lemail'])
    if user:
        if user[0].password == request.POST['Lpass']:
            request.session['email']=user[0].email
            return redirect('/success')
        return redirect("/")
    return redirect("/")