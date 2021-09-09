#core code was copied from stripe documentation

from django.contrib.auth.decorators import login_required
import stripe
import json
from django.http import HttpResponse
from shopping_cart.cart import Cart
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from shop_checkout.views import payment_confirmation
from django.shortcuts import render


# Create your views here.


@login_required
def CheckoutView(request):
    cart = Cart(request)
    total = str(cart.unit_total())
    total = total.replace('.', '')
    total = int(total)

    # API key from Stripe site

    stripe.api_key = 'sk_test_51JUDztBeU0R6ZOy2lywo6nuzKM9pPckoc3UjIhGdx4Shh0BwifLesRSy6dj3MQbMRryKPshBpeQUZO3WMzO0q0Ka00FmM7m3BQ'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'checkout/checkout.html', {'clinet_secret': intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        print(e)
        return HttpResponse(status=400)

        # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.objects.client_secret)
    
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)


class Error(TemplateView):
    template_name = 'checkout/error.html'
