from django.shortcuts import render
from django.http import HttpResponse
from .models import Rental
# Create your views here.
def home(request):
    return render(request, "rental/index.html")


def store(request):
    rentals = Rental.objects.all()
    for rental in rentals:
        img = rental.img
        name = rental.name
        rental_type = rental.rental_type
        rent_val = rental.rent_val
        rep_val = rental.rep_val
        quant = rental.quant
        print(img, name, rental_type, rent_val, rep_val,quant)

    return render(request, "rental/store.html", {
        'rentals': rentals
    })