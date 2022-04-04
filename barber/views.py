from unicodedata import name
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'barber/main.html')

def services(request):
    return render(request, 'barber/services.html')