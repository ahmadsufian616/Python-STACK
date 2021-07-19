from django.shortcuts import render, redirect
import random


def fun(request):
    if "number" not in request.session:
        request.session['number'] = random.randint(1, 100)
    

    return render(request, "index.html")

def fun2(request):
    if request.method == "POST":
        v= request.POST['name']

        if int(v)>request.session['number']:
            request.session['result'] = 'high'

        elif int(v)<request.session['number']:
            request.session['result'] = 'low'

        elif int(v)==request.session['number']:
            request.session['result']='equal'

    return redirect('/')

def fun3(request):
    del  request.session['number']
    return redirect('/')


