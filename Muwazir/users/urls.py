from django.urls import path
from . import views

app_name="users"

urlpatterns=[
    path("create/",views.create_user_account,name="create_user_account"),
]