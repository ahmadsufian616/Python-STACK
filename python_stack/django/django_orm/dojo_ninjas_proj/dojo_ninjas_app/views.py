from django.http import request
from django.shortcuts import render,redirect
from .models import dojos,ninjas

def fun(request):
    all_dojo=dojos.objects.all()
    context ={
        'all_dojo':all_dojo,
    }

    return render(request,"index.html",context)


def fun2(request):
        # name=request.POST["name"]
        # city=request.POST["city"]
        # state=request.POST["state"]
        dojos.objects.create(name=request.POST["name"],city=request.POST["city"],state=request.POST["state"])
        return redirect("/")


def fun3(request):
    d=request.POST['select_dojo']   
    ninjas.objects.create(fname=request.POST["fname"],lname=request.POST["lname"],dojo=dojos.objects.get(id=d))
    return  redirect("/")

    