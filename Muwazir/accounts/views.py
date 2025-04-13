from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from main.models import volunteer,booking
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login

# Create your views here.
def signup(request:HttpRequest):
   if request.method =="POST":
      try:
         new_user = User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],username=request.POST["username"],email=request.POST["email"])
         new_user.set_password(request.POST["password"])
         new_user.save()
         messages.success(request,"Registered user successfuly!","alert-success")
         return redirect("main:signin")
      except Exception as e:
         print(e)


   return render(request, 'main/signup.html')

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

def logout(request:HttpRequest):

   return render(request, 'main/logout.html')
