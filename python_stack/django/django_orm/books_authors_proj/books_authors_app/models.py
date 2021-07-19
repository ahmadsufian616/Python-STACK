from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

class Auther(models.Model):
    fname=models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    books=models.ManyToManyField(Book,related_name="authers")
    notes=models.CharField(max_length=255,null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
