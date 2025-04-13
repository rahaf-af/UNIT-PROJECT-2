from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from main.models import user,volunteer,booking

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
       

    return render(request, "users/update_profile.html",{"user":users})

def my_bookings(request: HttpRequest):
    bookings = booking.objects.filter(user_name=request.user)
    return render(request, 'main/my_bookings.html', {"bookings": bookings})

def volunteer_profile(request:HttpRequest ,volunteer_id:int):
    volunteers=volunteer.objects.get(pk=volunteer_id)
    return render(request, "users/volunteer_profile.html",{"volunteer":volunteers})

def rate_volunteer(request: HttpRequest, booking_id: int):
    book = booking.objects.get(id=booking_id)
    if request.method == "POST":
        rating = int(request.POST.get("rating"))
        book.rating = rating
        book.save()
        return redirect('main:my_bookings')
    return render(request, 'main/rate_volunteer.html', {"booking": book})