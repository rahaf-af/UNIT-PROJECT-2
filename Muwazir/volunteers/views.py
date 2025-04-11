from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from main.models import volunteer

# Create your views here.
def create_volunteer_account(request:HttpRequest):
    if request.method=="POST":
        print(request.POST["full_name"])
        new_volunteer=volunteer(full_name=request.POST["full_name"],gender=request.POST["gender"],nationality=request.POST["nationality"],phone_num=request.POST["phone_num"],email=request.POST["email"],Volunteering_site=request.POST["Volunteering_site"],service=request.POST["service"],profile_photo=request.FILES["profile_photo"])
        new_volunteer.save()
        return redirect('main:home')

    return render(request, "volunteers/create.html")

def login(request:HttpRequest):

    return render(request, "volunteers/login.html")


def volunteer_search(request:HttpRequest):

    return render(request, "volunteers/search.html")

def all_volunteers(request:HttpRequest):
    volunteers=volunteer.objects.all()
    return render(request, "volunteers/all.html",{"volunteers" : volunteers})

def volunteer_profile(request:HttpRequest ,volunteer_id:int):
    volunteers=volunteer.objects.get(pk=volunteer_id)
    return render(request, "volunteers/profile.html",{"volunteers":volunteer})

def update_profile(request:HttpRequest ,volunteer_id:int):
    volunteers=volunteer.objects.get(pk=volunteer_id)
    return render(request, "volunteers/update_profile.html",{"volunteers":volunteer})


    
