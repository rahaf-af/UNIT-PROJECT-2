from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import volunteer,booking


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
   return render(request, 'main/signin.html')

def signup(request:HttpRequest):
   return render(request, 'main/signup.html')

def bookings(request:HttpRequest ,volunteer_id:int):
   new_booking=booking.get(pk=volunteer_id)
   if request.method=="POST":
        booking.full_name=request.POST["full_name"]
        volunteers.gender=request.POST["gender"]
        volunteers.nationality=request.POST["nationality"]
        volunteers.phone_num=request.POST["phone_num"]
        volunteers.email=request.POST["email"]
        volunteers.Volunteering_site=request.POST["Volunteering_site"]
        volunteers.service=request.POST["service"]
        if "profile_photo" in request.FILES:
            volunteers.profile_photo=request.FILES["profile_photo"]
        volunteers.save()
        return redirect('volunteers:volunteer_profile',volunteer_id = volunteers.id)
   return render(request, 'main/bookings.html')