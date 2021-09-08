from django.shortcuts import render
from django.http.response import JsonResponse
from shopping_cart.cart import Cart
from shop_checkout.models import OrderDetails, UnitOrder


def ordered(request):
    cart = Cart(request)
    if request.POST.get('action') == 'ordered':
        user_id = request.user.id
        order_number = request.POST.get('order_number')
        carttotal = cart.unit_total()

        # check if the order is exists
        if OrderDetails.objects.filter(order_number).exists():
            pass
        else:
            order = OrderDetails.objects.create(
                user_id=user_id,
                title='title',
                first_name='firstname',
                last_name='lastname',
                address_line1='line1',
                address_line2='line2',
                town_or_city='town',
                country='country',
                unite_total=carttotal,
                order_number=order_number
             )
            order_id = order.pk
            for unit in cart:
                UnitOrder.objects.create(
                    order_id=order_id,
                    item=unit['item'],
                    price=unit['price'],
                    quanity=unit['quantity'],
                    size=unit['size']
                 )
            response = JsonResponse({'success': 'Order Created'})
            return response



