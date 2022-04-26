from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from .forms import BookingForm, ResumeForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def booking(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = BookingForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "The BARBERS"
            message = cd['first_name'] + ' ' + cd['last_name'] + ', Thank you for your inquiry about our booking service. We are currently providing top-rated service. In order to provide you an estimation of the cost of our services and more information, our manager will call you.'

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True
            messages.success(request, 'Message was send.')
            return redirect('main')

    else:
        form = BookingForm()
        messages.error(request, 'Something went wrong!!')

    return render(request, 'barber/booking.html', {

        'form': form,
        'messageSent': messageSent,

    })

# Create your views here.
def main(request):
    return render(request, 'barber/main.html')

def services(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, 'barber/services.html', context)

def faq(request):
    faqs = FAQ.objects.all()
    context = {'faqs': faqs}
    return render(request, 'barber/faq.html', context)


def join(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ResumeForm()
    
    return render(request, 'barber/join_our_team.html', {'form': form})


def team(request):
    barbers = Barbers.objects.all()
    return render(request, 'barber/our_team.html', {'barbers': barbers})

def about(request):
    comments = Comments.objects.all()
    context = {'comments': comments}
    return render(request, 'barber/about.html', context)