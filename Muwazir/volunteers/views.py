from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from main.models import volunteer,booking

# Create your views here.
def create_volunteer_account(request:HttpRequest):
    if request.method=="POST":
        try:
            new_volunteer = volunteer(
                full_name=request.POST.get("full_name"),
                gender=request.POST.get("gender"),
                nationality=request.POST.get("nationality"),
                phone_num=request.POST.get("phone_num"),
                email=request.POST.get("email"),
                Volunteering_site=request.POST.get("Volunteering_site"),
                service=", ".join(request.POST.getlist("service")),  # <-- مهم هنا
                profile_photo=request.FILES.get("profile_photo")
            )
            new_volunteer.save()
            return redirect("main:home")
        except Exception as e:
            print(f"Error creating volunteer: {e}")
    return render(request, "volunteers/create.html")

def login(request:HttpRequest):

    return render(request, "volunteers/login.html")


def volunteer_search(request:HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >=1: 
        volunteers=volunteer.objects.filter(service__contains=request.GET["search"])
    else:
        volunteers=[]

    return render(request, "volunteers/search.html")

def all_volunteers(request:HttpRequest):
    volunteers=volunteer.objects.all()
    return render(request, "volunteers/all.html",{"volunteers" : volunteers})

def volunteer_profile(request:HttpRequest ,volunteer_id:int):
    volunteers=volunteer.objects.get(pk=volunteer_id)
    return render(request, "volunteers/profile.html",{"volunteer":volunteers})

def update_profile(request:HttpRequest ,volunteer_id:int):
    volunteers=volunteer.objects.get(pk=volunteer_id)
    if request.method=="POST":
        volunteers.full_name=request.POST["full_name"]
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
       

    return render(request, "volunteers/update_profile.html",{"volunteer":volunteers})

def delete_profile(request:HttpRequest ,volunteer_id:int):
    volunteers=volunteer.objects.get(pk=volunteer_id)
    volunteers.delete()
    
    return redirect("main:singup")

def availability(request:HttpRequest ,volunteer_id:int):
    volunteers=volunteer.objects.get(pk=volunteer_id)
    volunteers.is_available=not volunteers.is_available
    volunteers.save()
    return redirect("volunteers:volunteer_profile",volunteer_id=volunteer_id)

def my_bookings(request:HttpRequest ,volunteer_id:int):

   return render(request, "volunteers/update_profile.html") 

def volunteer_bookings(request: HttpRequest):
    bookings = booking.objects.filter(volunteer_name=request.user.volunteer)
    return render(request, 'volunteer/volunteer_bookings.html', {"bookings": bookings})
