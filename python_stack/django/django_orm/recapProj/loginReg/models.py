from django.db import models
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class usermanager(models.Manager):
    def v(self,postData):
        errors={}
        if len(postData['first'])<2 :
            errors['first']="first name must be at least 2 char"
        
        if postData['first'].isalpha()!=True :
            errors['first']="char only "

        if len(postData['last'])<2:
            errors['last']="last name must be al least 2 char "
        
        if postData['last'].isalpha()!=True :
                errors['last']="char only "

        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"
        if len(postData['pass'])<8:
            errors['pass']="must more than 8"

        if postData['pass']!=postData['cpass']:
            errors['pass']="not the same password"
        

        return errors
        



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=usermanager()



# def login_validator(self, postData):
#     errors2 = {}
#     email2 = postData['email2']
#     password2 = postData['password2']
#     usr = User.objects.filter(email=email2)
 