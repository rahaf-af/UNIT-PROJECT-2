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
   
def bookings(request: HttpRequest, volunteer_id: int):
    volunteers = volunteer.objects.get(pk=volunteer_id)

    if request.method == "POST":
        
        current_user = request.user
        selected_volunteer = volunteer.objects.get(id=volunteer_id)
        date = request.POST.get("date")
        time = request.POST.get("time")
        location = request.POST.get("location")
        notes = request.POST.get("notes")

        if not date or not time or not location:
            messages.error(request, "Please fill in all required fields.")
            return render(request, 'main/bookings.html', {"volunteer": volunteers})

        new_booking = booking(
            user_name=request.user,
            volunteer_name=selected_volunteer,
            date=date,
            time=time,
            location=location,
            notes=notes
        )
        
        new_booking.save()
        messages.success(request, "Reservation created successfully.")
        return redirect('volunteers:volunteer_profile', volunteer_id=volunteers.id)

    return render(request, 'main/bookings.html', {"volunteer": volunteers})
