from unicodedata import name
from django.shortcuts import render
from .models import Services

# Create your views here.
def main(request):
    return render(request, 'barber/main.html')

def services(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, 'barber/services.html', context)