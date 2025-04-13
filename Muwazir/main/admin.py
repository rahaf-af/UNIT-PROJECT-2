from django.contrib import admin
from .models import user ,volunteer,booking

# Register your models here.
admin.site.register(user)
admin.site.register(volunteer)
admin.site.register(booking)