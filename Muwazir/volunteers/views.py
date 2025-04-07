from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from main.models import volunteer

# Create your views here.
def create_volunteer_account(request:HttpRequest):
    
    return render(request, "volunteers/create.html")

def volunteer_search(request:HttpRequest):

    return render(request, "volunteers/search.html")

    
