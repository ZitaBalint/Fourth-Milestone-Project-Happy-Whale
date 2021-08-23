from django.shortcuts import render


# Create your views here.


def cart_total(request):
    return render(request, 'cart/cart.html')
