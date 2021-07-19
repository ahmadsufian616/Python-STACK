from django.db import models

# class Movie(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField()
#     release_date = models.DateTimeField()
#     duration = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class person(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    age=models.IntegerField()
    birthday=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class users(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    age=models.IntegerField()
    email=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

