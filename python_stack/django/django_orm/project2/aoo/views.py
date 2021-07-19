from django.shortcuts import render , redirect
from .models import users

def fun(request):
    context ={
        'users':users.objects.all()
    }

    return render(request,"index.html",context)



def fun1(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        users.objects.create(name=name,age=age,email=email)
    return redirect("/")
    

