# core code was copied from stripe documentation

import json

import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic.base import TemplateView

from shop_checkout.views import payment_confirmation
from shopping_cart.cart import Cart

# Create your views here.

endpoint_secret = settings.STRIPE_WH_SECRET


@login_required
def CheckoutView(request):
    cart = Cart(request)
    total = str(cart.unit_total())
    total = total.replace('.', '')
    total = int(total)

    # API key from Stripe site

    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': (request.user).id}
    )
    print('kakas')
    return render(request, 'checkout/checkout.html', {'client_secret': intent.client_secret})


@require_POST
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    endpoint_secret = settings.STRIPE_WH_SECRET

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key, sig_header,
            endpoint_secret
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
