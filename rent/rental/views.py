from django.shortcuts import render
from django.http import HttpResponse
from .models import Rental
# Create your views here.
def home(request):
    return render(request, "rental/index.html")


def store(request):
    all_rentals = Rental.objects.all()
    return render(request, "rental/store.html")