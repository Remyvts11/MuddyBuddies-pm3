from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    table_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # prevent exact same table/date/time double booking
        conflicts = Booking.objects.exclude(pk=self.pk).filter(
            date=self.date,
            time=self.time,
            table_number=self.table_number
        )
        if conflicts.exists():
            raise ValidationError("That table is already booked for this date and time.")

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
