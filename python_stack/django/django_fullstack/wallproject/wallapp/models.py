from django.db import models


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


class users (models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    objects = UserManager()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class masseges (models.Model):
    massege = models.TextField(max_length=1000)
    user = models.ForeignKey(users, related_name='msg',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class comments (models.Model):
    comment = models.TextField(max_length=1000)
    massage = models.ForeignKey(
        masseges, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        users, related_name='comments', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
