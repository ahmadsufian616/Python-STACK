from django.shortcuts import render,redirect
from .models import users,Book
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    if id in request.session:
        redirect('/book')
    return render (request,"index.html")

def create_user (request):
    error=users.objects.reg_validation(request.POST)
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
            return redirect("/")
    request.session['name']=request.POST['first']
    request.session['email']=request.POST['email']
    users.objects.create(First_Name=request.POST['first'],Last_Name=request.POST['last']
    ,Email=request.POST['email'],Password=pw_hash)
    last_user=users.objects.last()
    request.session['id']=last_user.id

    return redirect ("/")

def logs(request):
    
    user = users.objects.filter(Email=request.POST['Email'])
    if user:
        if bcrypt.checkpw(request.POST['password'].encode(), user[0].Password.encode()):
            request.session['email']=user[0].Email 
            request.session['name']=user[0].First_Name
            request.session['id']=user[0].id
            return redirect('/book')
        return redirect("/")
    return redirect("/")

    

def book(request):
    all_book=Book.objects.all()
    context={
        'all_book':all_book,
    }
    
    return render(request,"book.html",context)

def addbook(request):
    error=users.objects.book_validation(request.POST)

    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
            return redirect("/book")
    user=request.session['id']
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],uploaded_by=users.objects.get(id=user))
    user=users.objects.get(id=request.session['id'])
    user.liked_books.add(Book.objects.last())
    return redirect('/book')
    

def bookdesc(request,i):
    book=Book.objects.get(id=i)
    user = users.objects.get(id=request.session['id'])
    liked_books = book.users_who_like.all()
    data={
        "book":book,
        "liked_books":liked_books,
        "user":user,
    }
    return render (request,"bookdesc.html",data)

def edit (request,i):
    if request.POST:

        if  'edit'in request.POST:
            t=Book.objects.get(id=i)
            t.title=request.POST['newtitle']
            t.save()
            d=Book.objects.get(id=i)
            d.desc=request.POST['newdesc']
            d.save()

        if 'delete' in request.POST:
            book=Book.objects.get(id=i)
            book.delete()
            return redirect('/book')
    return redirect(f'/bookdesc/{i}')


def logout(request):
    del request.session['email']
    del request.session['name']
    del request.session['id']
    return redirect("/")

def like_book(request,i):
    user=users.objects.get(id=request.session['id'])
    book=Book.objects.get(id=i)
    user.liked_books.add(book)
    return redirect ('/book')

