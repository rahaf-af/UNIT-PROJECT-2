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


class booking(models.Model):
    user_name = models.ForeignKey(user, on_delete=models.CASCADE, related_name='reservations')
    volunteer_name= models.ForeignKey(volunteer, on_delete=models.CASCADE, related_name='reservations')
    date= models.DateField()
    time= models.TimeField()
    location= models.CharField(max_length=200)
    notes= models.TextField(blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')
    rating = models.IntegerField(null=True, blank=True , choices=[
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),])
   
 

    def __str__(self):
        return f"{self.user.username} - {self.volunteer.user.username} - {self.date}"


