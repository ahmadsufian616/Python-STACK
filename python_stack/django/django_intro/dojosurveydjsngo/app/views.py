from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def fun2(request):
    name= request.POST['name']
    loc= request.POST['loc']
    lan= request.POST['lan']
    com= request.POST['com']
    context = {
    	    "name" : name,
    	    "loc" : loc,
            "lan":lan,
            "com":com
    }

    return render(request,'result.html',context)

