from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here
def user_type(request:HttpRequest):
   return render(request, 'main/user_type.html')

def home(request:HttpRequest):
    response= render (request, 'main/home.html')
    response.set_cookie("name","value")
    return response

def about(request:HttpRequest):
   return render(request, 'main/about.html')

def contact(request:HttpRequest):
   return render(request, 'main/contact.html')

def faq(request:HttpRequest):
   return render(request, 'main/faq.html')
   
