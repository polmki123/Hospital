from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
#class CustomUserAdmin(UserAdmin):
#    form = CustomUserCreationForm

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Treatment)
admin.site.register(Reservation)
