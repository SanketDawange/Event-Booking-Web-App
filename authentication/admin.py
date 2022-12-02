from django.contrib import admin
from .models import AllEvent
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name','booked_seats','total_seats')

admin.site.register(AllEvent, EventAdmin)