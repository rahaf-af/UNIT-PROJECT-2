from django.urls import path
from . import views

app_name="users"

urlpatterns=[
    path("create/",views.create_user_account,name="create_user_account"),
    path("profile/<user_id>",views.user_profile,name="user_profile"),
    path("delete<int:user_id>/",views.delete_profile,name="delete_profile"),
    path("my_bookings/",views.user_bookings,name="user_bookings"),
    path("update_profile/",views.update_profile,name="update_profile"),
    path("volunteer_profile/<int:volunteer_id>/",views.volunteer_profile,name="volunteer_profile"),
]