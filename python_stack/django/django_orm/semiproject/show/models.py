from django.db import models


class Showmanager(models.Manager):    
    def basic_validator(self, postData):
        error={}
        if len(postData['Title']) < 2:#data from form 
            error["name"] ="The Show Title must be  at least 2 characters"
        if len(postData["network"])<3:
            error["network"]="The Show Network must be at least 3 characters"
        if len(postData['desc']) < 10:
            error["desc"] = "Blog description should be at least 10 characters"
        return error

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    date=models.DateField()
    desc=models.TextField(max_length=1000)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    objects=Showmanager()
