from django.urls import path
from . import views

app_name="volunteers"

urlpatterns=[
   path("create/",views.create_volunteer_account,name="create_volunteer_account"),
   path("search/",views.volunteer_search,name="volunteer_search"),
]