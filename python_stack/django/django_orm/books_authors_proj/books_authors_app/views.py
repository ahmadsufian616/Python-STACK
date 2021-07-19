from django.shortcuts import render, redirect
from .models import Book, Auther


def fun(request):
    all_book = Book.objects.all()
    context = {
        'all_book': all_book,
    }
    return render(request, "index.html", context)


def fun2(request):
    all_aurther = Auther.objects.all()
    context = {
        'all_aurther': all_aurther,
    }
    return render(request, "authers.html", context)


def ADDBOOK(request):
    title = request.POST["title"]
    desc = request.POST["desc"]
    Book.objects.create(title=title, desc=desc)
    return redirect("/")


def ADDAUTHERS(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    note = request.POST["note"]
    Auther.objects.create(fname=fname, lname=lname, notes=note)
    return redirect("/authers")


def viewbook(request):
    all_aurther = Auther.objects.all()
    t = request.POST['title1']
    d = request.POST['desc1']
    i = request.POST['ID']
    context = {
        'title': t,
        'desc': d,
        'ID': i,
        'all_aurther': all_aurther,
    }

    return render(request, "viewbook.html", context)


def viewaurther(request):
    all_book = Book.objects.all()
    request.session['name']= request.POST['allname']
    name=request.session['name']
    request.session['Id'] = request.POST['ID']
    ID=request.session['Id']
    request.session['note'] = request.POST['note']
    note=request.session['note']
    context = {
        'name': name,
        'ID': ID,
        'note': note,
        'all_book': all_book,
    }
    return render(request, "viewaurther.html", context)


def assignBook(request):
    a=request.POST["select_book"]
    b=request.POST["ID"]
    this_book = Book.objects.get(id=a)
    this_aurther = Auther.objects.get(id=b)
    this_aurther.books.add(this_book)
    return redirect("/viewaruther")
    pass

def assignaurther(request):
    aurther=request.POST["select_auther"]
    id=request.POST["ID"]
    this_aurther=Auther.objects.get(id=aurther)
    this_book=Book.objects.get(id=id)
    this_book.authers.add(this_aurther)
    return redirect ('/viewbook')