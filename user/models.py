from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
 

class AddressInfo(models.Model):
    ufullname = models.CharField(max_length=20)
    uaddress = models.CharField(max_length=100)
    uzipcode = models.CharField(max_length=6,default='000000')
    utel = models.CharField(max_length=11) 
    is_default = models.BooleanField(default = False)
    auser = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
