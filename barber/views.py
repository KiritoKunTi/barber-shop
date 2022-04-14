from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from .models import *

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