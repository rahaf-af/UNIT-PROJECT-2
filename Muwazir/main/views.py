from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import volunteer,booking
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login

# Create your views here
def user_type(request:HttpRequest):
   return render(request, 'main/user_type.html')

def home(request:HttpRequest):
   volunteers=volunteer.objects.all()[0:3]
    
   return render(request, 'main/home.html',{"volunteers" : volunteers})

def about(request:HttpRequest):
   return render(request, 'main/about.html')

def contact(request:HttpRequest):
   return render(request, 'main/contact.html')

def faq(request:HttpRequest):
   return render(request, 'main/faq.html')
   
def services(request:HttpRequest):

   return render(request, 'main/services.html')

def signin(request:HttpRequest):
   if request.method == "POST":
      user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
      if user:
         login(request ,user)
         messages.success(request,"Logged in successfuly!","alert-success")
         return redirect("main:home")
      else:
         messages.error(request, "please try again, your credentials are wrong" ,"alert-danger" )

   return render(request, 'main/signin.html')

def signup(request:HttpRequest):
   if request.method =="POST":

      try:
         new_user = User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],username=request.POST["username"],email=request.POST["email"])
         new_user.set_password(request.POST["password"])
         new_user.save()
         messages.SUCCESS(request,"Registered user successfuly!","alert-success")
         return redirect("main:signin")
      except Exception as e:
         print(e)


   return render(request, 'main/signup.html')

def logout(request:HttpRequest):

   return render(request, 'main/logout.html')
   
def bookings(request:HttpRequest ,volunteer_id:int):
   volunteers=volunteer.get(pk=volunteer_id)
   if request.method=="POST":
        new_booking=booking(date=request.POST["date"],time=request.POST["time"],nationality=request.POST["nationality"],location=request.POST["location"],notes=request.POST["notes"])
        new_booking.save()
        return redirect('volunteers:volunteer_profile',volunteer_id = volunteers.id)
   return render(request, 'main/bookings.html')

