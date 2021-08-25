from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .cart import Cart
from django.http import JsonResponse
from shop.models import Item

# Create your views here.


def cart_total(request):
    return render(request, 'cart/cart.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('itemid'))
        item_size = int(request.POST.get('itemsize'))
        item_quantity = int(request.POST.get('itemquantity'))
        item = get_object_or_404(Item, pk=item_id)
        cart.add(item=item, size=item_size, quantity=item_quantity)
        response = JsonResponse({})
        return response
