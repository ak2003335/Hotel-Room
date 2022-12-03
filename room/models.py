from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    dob = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.user.username


class room(models.Model):
    room_no= models.CharField(max_length=20,null=True,unique=True)
    price= models.CharField(max_length=20,null=True)
    r_type= models.CharField(max_length=20,null=True)
    r_status= models.CharField(max_length=30,null=True)
    r_image= models.FileField(null=True)
class ajeetdb(models.Model):
    First_name=models.CharField(max_length=20,null=True,unique=True)
    Last_name=models.CharField(max_length=20,null=True)



