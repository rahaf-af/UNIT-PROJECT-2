from django.db import models

# Create your models here.
class user(models.Model):
    profile_photo=models.ImageField(upload_to="images/" ,default="images/profil photo.jpg")
    full_name=models.CharField(max_length=100)
    phone_num=models.IntegerField()
    gender=models.CharField(max_length=100,default='M')
    email=models.EmailField()
    nationality=models.CharField(max_length=512)

    def __str__(self)-> str:
        return self.full_name 


class volunteer(models.Model):
    profile_photo=models.ImageField(upload_to="images/" ,default="images/profil photo.jpg")
    full_name=models.CharField(max_length=100)
    phone_num=models.IntegerField()
    gender=models.CharField(max_length=100,default='M')
    email=models.EmailField()
    nationality=models.CharField(max_length=100)
    experiences=models.TextField()
    service=models.CharField(max_length=100)
    Volunteering_site=models.CharField(max_length=100,default="The holy mosque")
    is_available=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    ratings=models.SmallIntegerField(default=0)
    def __str__(self)-> str:
        return self.full_name 


    



#class booking(models.Model):

