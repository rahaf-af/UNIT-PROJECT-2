from django.urls import path
from . import views

app_name="volunteers"

urlpatterns=[
   path("create/",views.create_volunteer_account,name="create_volunteer_account"),
   path("search/",views.volunteer_search,name="volunteer_search"),
   path("all/",views.all_volunteers,name="all_volunteers"),
   path("profile/<int:volunteer_id>/",views.volunteer_profile,name="volunteer_profile"),
   path("update/<int:volunteer_id>/",views.update_profile,name="update_profile"),
   path("delete<int:volunteer_id>/",views.delete_profile,name="delete_profile"),
   path("bookings/<int:volunteer_id>/",views.volunteer_bookings,name="bookings"),
   path("availability/<int:volunteer_id>",views.availability,name="availability"),
   
]