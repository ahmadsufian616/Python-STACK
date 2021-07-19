from django.shortcuts import render,redirect
from .models import users,masseges,comments
from django.contrib import messages
import bcrypt

# Create your views here.
def login(request):
    return render(request,"Login.html")

def Register(request):
    return render(request,"Register.html")

def create_users(request):
    error=users.objects.reg_validation(request.POST)
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
            return redirect("/Register")
    request.session['name']=request.POST['first']
    request.session['email']=request.POST['email']
    users.objects.create(First_Name=request.POST['first'],Last_Name=request.POST['last']
    ,Email=request.POST['email'],Password=pw_hash)
    last_user=users.objects.last()
    request.session['id']=last_user.id
    
    return redirect('/')  
     
def log(request):
    user = users.objects.filter(Email=request.POST['Email'])
    if user:
        if bcrypt.checkpw(request.POST['password'].encode(), user[0].Password.encode()):
            request.session['email']=user[0].Email 
            request.session['name']=user[0].First_Name
            request.session['id']=user[0].id
            return redirect('/wall')
        return redirect("/")
    return redirect("/")

def walldisplay(request):
    all_msg=masseges.objects.all()
    all_com=comments.objects.all()
    context={
        "all_msg":all_msg,
        "all_com":all_com,
    }
    return render (request,"wall.html",context)
def logout(request):
    del request.session['email']
    del request.session['name']
    del request.session['id']
    return redirect("/")

def create_post(request):
    user=request.session['id']
    
    masseges.objects.create(massege=request.POST['post'],user=users.objects.get(id=user))
    last_msg=masseges.objects.last()
    request.session['msgs']=last_msg.id

    return redirect('/wall')

def create_comment(request,i):
    user=request.session['id']
    comments.objects.create(comment=request.POST['post_com'],massage=masseges.objects.get(id=i),user=users.objects.get(id=user))
    return redirect('/wall')