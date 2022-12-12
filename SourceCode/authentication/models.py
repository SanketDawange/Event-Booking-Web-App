from django.db import models

# Create your models here.
class AllEvent(models.Model):
    # any event has following attributes
    # event name, date, place, total seats, booked seats, hostname
    event_name = models.CharField(max_length=50)
    host_name = models.CharField(max_length=50)
    event_place = models.CharField(max_length=100, default="")
    event_description = models.CharField(max_length=500)
    event_date = models.DateField()
    seat_price = models.IntegerField(default=0)
    total_seats = models.IntegerField()
    booked_seats = models.IntegerField()

