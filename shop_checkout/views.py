from django.shortcuts import render
from django.http.response import JsonResponse
from shopping_cart.cart import Cart
from . models import OrderDetails, UnitOrder


def Ordered(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        # userid = request.user.id
        order_key = request.POST.get('order_key')
        carttotal = cart.unit_total()

        # check if the order is exists
        if OrderDetails.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = OrderDetails.objects.create(
                title='title',
                first_name='firstName',
                last_name='lastName',
                address_line1='line1',
                address_line2='line2',
                town_or_city='town',
                country='country',
                unit_total=carttotal,
                order_key=order_key
             )
            order_id = order.pk

            for unit in cart:
                UnitOrder.objects.create(
                    order_id=order_id,
                    item=unit['item'],
                    unit_total=unit['price'],
                    quantity=unit['quantity'],
                    unit_size=unit['size']
                 )
            response = JsonResponse({'success': 'Order Created'})
            return response


def payment_confirmation(data):
    OrderDetails.objects.filer(order_key=data).update(billing_status=True)


def order_sent(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'shop_checkout/ordersent.html')
