from django.contrib import admin
from .models import Reservation

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    search_fields = ['NAME']
    search_fields = ['HOSPITAL']
    search_fields = ['VACCINE']
    search_fields = ['DATE']
    search_fields = ['HOUR']
    
    
admin.site.register(Reservation, ReservationAdmin)

