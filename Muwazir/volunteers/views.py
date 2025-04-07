from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from main.models import volunteer

# Create your views here.
def create_volunteer_account(request:HttpRequest):
    if request.method=="POST":
        new_volunteer=volunteer(full_name=request.POST["full_name"],gender=request.POST["gender"],nationality=request.POST["nationality"],phone_num=request.POST["phone_num"],email=request.POST["email"],Volunteering_site=request.POST["Volunteering_site"],service=request.POST["service"])


    
    return render(request, "volunteers/create.html")

def volunteer_search(request:HttpRequest):

    return render(request, "volunteers/search.html")

    
