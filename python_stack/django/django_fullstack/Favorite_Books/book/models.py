from django.contrib.messages.api import error
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = {}
        if len(postData['first']) <= 0:
            errors["first"] = "Must enter your first name!"
        elif len(postData['last']) < 2:
            errors["last"] = "First name should be at least 2 characters!"
        if len(postData['last']) <= 0:
            errors["last"] = "Must enter a last name!"
        elif len(postData['last']) < 2:
            errors["last"] = "Last name should be at least 2 characters!"
        if len(postData['password']) <= 0:
            errors["password"] = "Password is required!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        if len(postData['email']) <= 0:
            errors["email"] = "Email is required!"
        if users.objects.filter(Email=postData['email']).exists():
            errors['email'] = "Email already exists."
        # if User.objects.filter(password = postData['pword']).exists():
        #     errors['pword'] = "Password already in use"
        if postData['confirm'] != postData['password']:
            errors['confirm'] = "Confirmation password does not match password!"
        
        return errors


    def book_validation(self, postData):
        error={}
        if len(postData['title'])<0:
            error['title']="you must enter the title"
        if len(postData['desc'])<5:
            error['desc']="desc must be at least 5 characters"
        return error

class users (models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    objects = UserManager()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # liked_books = a list of books a given user likes
    # books_uploaded = a list of books uploaded by a given user
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField()
    uploaded_by=models.ForeignKey(users,related_name="books_uploaded",on_delete=models.CASCADE)
    users_who_like =models.ManyToManyField(users,related_name="liked_books")
    objects = UserManager()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    # uploaded_by = user who uploaded a given book
    # users_who_like = a list of users who like a given book

