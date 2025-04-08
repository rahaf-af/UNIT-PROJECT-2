from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import volunteer


# Create your views here
def user_type(request:HttpRequest):
   return render(request, 'main/user_type.html')

def home(request:HttpRequest):
   volunteers=volunteer.objects.all()
    
   return render(request, 'main/home.html',{"volunteers" : volunteers})

def about(request:HttpRequest):
   return render(request, 'main/about.html')

def contact(request:HttpRequest):
   return render(request, 'main/contact.html')

def faq(request:HttpRequest):
   return render(request, 'main/faq.html')
   
