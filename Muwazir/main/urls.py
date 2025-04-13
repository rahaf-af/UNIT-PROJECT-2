from django.urls import path
from . import views

app_name="main"

urlpatterns=[
             path("user_type/" ,views.user_type , name="user_type"),
             path("home/" ,views.home , name="home"),
             path("about/" ,views.about , name="about"),
             path("contact/" ,views.contact , name="contact"),
             path("faq/" ,views.faq, name="faq"),
             path("services/" ,views.services, name="services"),
             path("signin/" ,views. signin, name="signin"),
             path("signup/" ,views. signup, name="signup"),
             path('bookings/<int:volunteer_id>/', views.bookings, name='bookings'),
             ]