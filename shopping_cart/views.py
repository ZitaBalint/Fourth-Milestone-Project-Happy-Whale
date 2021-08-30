from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .cart import Cart
from django.http import JsonResponse
from shop.models import Item

# Create your views here.


def cart_total(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        item_id = str(request.POST.get('itemid'))
        item_size = str(request.POST.get('itemsize'))
        item_quantity = int(request.POST.get('itemquantity'))
        item = get_object_or_404(Item, id=item_id)
        cart.add(item=item, quantity=item_quantity, size=item_size)

        cartquantity = cart.__len__()
        response = JsonResponse({
            'quantity': cartquantity,
            'size': item_size
        })
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        item_id = str(request.POST.get('itemid'))
        cart.delete(item=item_id)
        cartquantity = cart.__len__()
        
        carttotal = cart.unit_total()
        response = JsonResponse({
            'quantity': cartquantity,
            'total': carttotal
        })
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('itemid'))
        item_quantity = int(request.POST.get('itemquantity'))
        item_size = str(request.POST.get('itemsize'))
        cart.update(item=item_id, quantity=item_quantity, size=item_size)
        # cartsubtotal = cart.subtotal()
        cartquantity = cart.__len__()
        carttotal = cart.unit_total()
        response = JsonResponse({
            'quantity': cartquantity,
            'total': carttotal,
            # 'subtotal': cartsubtotal
        })
        return response
