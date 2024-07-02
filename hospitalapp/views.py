from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
import requests
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request,'index.html')
def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']
        date = request.POST['date']
        message = request.POST.get('message', '')

        appointment = Appointment(
            name=name,
            email=email,
            phone=phone,
            department=department,
            date=date,
            message=message
        )
        appointment.save()

        subject = 'Appointment Confirmation'
        message_body = f"Dear {appointment.name},\n\nYour appointment for the {appointment.department} department on {appointment.date} has been confirmed.\n\nThank you,\nHospital Management"
        from_email = 'aa0676505@gmail.com'
        recipient_list = [appointment.email]

        send_mail(subject, message_body, from_email, recipient_list)

        return HttpResponse("Appointment booked successfully and acknowledgment sent.")
    else:
        return render(request, 'form.html')
    

def view_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment.html', {'appointments': appointments})