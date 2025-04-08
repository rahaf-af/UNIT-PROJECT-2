from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from main.models import user

# Create your views here.
def create_user_account(request:HttpRequest):
    if request.method=="POST":
        new_user=user(full_name=request.POST["full_name"],gender=request.POST["gender"],nationality=request.POST["nationality"],phone_num=request.POST["phone_num"],email=request.POST["email"],profile_photo=request.FILES["profile_photo"])
        new_user.save()


        return redirect('main:home')

    return render(request, "users/create.html")
