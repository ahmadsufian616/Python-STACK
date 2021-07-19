from django.db import models

class dojos(models.Model):
    name=models.CharField(max_length=45)
    city=models.CharField(max_length=45)
    state=models.CharField(max_length=45)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
class ninjas(models.Model):
    fname=models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    dojo=models.ForeignKey(dojos,related_name="d",on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

