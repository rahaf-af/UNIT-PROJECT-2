from django.db import models

# Create your models here.
class user(models.Model):
    full_name=models.CharField(max_length=512)
    phone_num=models.IntegerField()
    gender=models.CharField(max_length=512 ,default='M')
    email=models.EmailField()
    nationality=models.CharField(max_length=512) 

class volunteer(models.Model):
    full_name=models.CharField(max_length=512)
    phone_num=models.IntegerField()
    gender=models.CharField(max_length=512 , default='M')
    email=models.EmailField()
    nationality=models.CharField(max_length=512)
    experiences=models.TextField()
    service=models.CharField(max_length=512)
    is_available=models.BooleanField()
    is_verified=models.BooleanField()
    ratings=models.SmallIntegerField(default=0)


    



#class booking(models.Model):

