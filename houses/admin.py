from django.contrib import admin
from .models import LandLords, Houses, CareTaker, Teenants 

# Register your models here.
models_to_register = [LandLords, Houses, CareTaker, Teenants]
admin.site.register(models_to_register)