from django.db import models

class users(models.Model):
    name=models.CharField(max_length=45)
    email=models.TextField()
    age=models.IntegerField()