from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Rental
from django.contrib import messages
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

def rent(request, item_id):
    rental = Rental.objects.get(pk=item_id)
    if rental.quant > 0:
        rental.quant -= 1
        messages.success(request, "You have rented " + rental.name + "!")
        rental.save()
    return redirect('store')



def returns(request, item_id):
    rental = Rental.objects.get(pk=item_id)
    rental.quant += 1
    messages.success(request, "You have returned " + rental.name + "!")
    rental.save()
    return redirect('store')
