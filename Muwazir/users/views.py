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

def user_profile(request:HttpRequest  ,user_id:int):
    users=user.objects.get(pk=user_id)

    return render(request, "users/profile.html",{"users":user})

def delete_profile(request:HttpRequest ,user_id:int):
    users=user.objects.get(pk=user_id)
    users.delete()
    
    return redirect("main:singup")

def update_profile(request:HttpRequest ,user_id:int):
    users=user.objects.get(pk=user_id)
    if request.method=="POST":
        users.full_name=request.POST["full_name"]
        users.gender=request.POST["gender"]
        users.nationality=request.POST["nationality"]
        users.phone_num=request.POST["phone_num"]
        users.email=request.POST["email"]
        if "profile_photo" in request.FILES:
            users.profile_photo=request.FILES["profile_photo"]
            users.save()
        return redirect('users:user_profile',users_id = users.id)
       

    return render(request, "volunteers/update_profile.html",{"user":users})

