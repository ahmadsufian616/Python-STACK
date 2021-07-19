
from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages
import bcrypt


# Create your views here.
# def index(request):
# return render(request,"Addnewshow.html")
def showall(request):
    context = {
        "all_show": Show.objects.all()
    }
    return render(request, "Allshow.html", context)


def Addnewshow(request):
    return render(request, "Addnewshow.html")

    


def create(request):
    error=Show.objects.basic_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['Title'], network=request.POST['network'], date=request.POST['Date'],
         desc=request.POST['desc'])
        lastshow = Show.objects.last()
        id = lastshow.id
        return redirect(f"/shows/{id}")

   

        # title=request.POST["Title"]
        # network=request.POST["network"]
        # date=request.POST["Date"]
        # desc=request.POST["desc"]
    #     Show.objects.create(title=request.POST["Title"], network=request.POST["network"],
    #                         date=request.POST["Date"], desc=request.POST["desc"])
    #     lastshow = Show.objects.last()
    #     id = lastshow.id
    # return redirect(f"/shows/{id}")


def show(request, i):
    show = Show.objects.get(id=i)
    context = {
        "show": show
    }
    return render(request, "show.html", context)


def edit(request, i):
    show = Show.objects.get(id=i)
    context = {
        "show": show
    }
    return render(request, "edit.html", context)


def update(request, i):
    error=Show.objects.basic_validator(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/shows/new')

    if request.method == "POST":
        title = request.POST["Title"]
        network = request.POST["network"]
        date = request.POST["Date"]
        desc = request.POST["desc"]
    show = Show.objects.get(id=i)
    show.title = title
    show.network = network
    show.date = date
    show.desc = desc
    show.save()
    return redirect("/shows/")


def delete(request, i):
    show = Show.objects.get(id=i)
    show.delete()
    return redirect('/shows')
