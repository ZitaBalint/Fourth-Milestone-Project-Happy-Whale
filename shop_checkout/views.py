import stripe
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shopping_cart.cart import Cart


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