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
        item_id = request.POST.get('itemid')
        item_size = request.POST.get('itemsize')
        item_quantity = request.POST.get('itemquantity')
        item = get_object_or_404(Item, id=item_id)
        cart.add(item=item, size=item_size, quantity=item_quantity)
        response = JsonResponse({
            'quantity': item_quantity,
            'size': item_size
        })
        return response
