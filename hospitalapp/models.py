from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    date = models.DateField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.department} on {self.date}"