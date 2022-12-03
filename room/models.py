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



class Contact(models.Model):
    con_name = models.CharField(max_length=20,null=True)
    con_mobile = models.CharField(max_length=30, null=True)
    con_email = models.CharField(max_length=10,null=True)
    con_purpose = models.CharField(max_length=15,null=True)


class Booked(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=20,null=True)
    mobile1 = models.CharField(max_length=20,null=True)
    mobile2 = models.CharField(max_length=20,null=True)
    booking_date = models.CharField(max_length=20,null=True)
    days = models.CharField(max_length=20,null=True)
    price = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=20,null=True)
    status = models.CharField(max_length=20,null=True)
class aj(models.Model):
    x=models.IntegerField(max_length=1000,null=True)
    y=models.IntegerField(max_length=1000,null=True)



