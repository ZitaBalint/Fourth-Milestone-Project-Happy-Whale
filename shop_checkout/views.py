from django.http.response import JsonResponse
from django.shortcuts import render
import stripe
from django.conf import settings
from shopping_cart.cart import Cart
from profiles.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderDetails, UnitOrder
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect


from django import forms


class CheckOutForm(forms.ModelForm):

    class Meta:
        model = OrderDetails
        fields = (
            'title',
            'first_name',
            'last_name',
            'email_address',
            'address_line1',
            'address_line2',
            'town_or_city',
            'country',
            'postcode',
            'unit_total',
        )
        widgets = {"unit_total": forms.HiddenInput()}


class CheckoutFormView(CreateView, LoginRequiredMixin):
    template_name = 'checkout/checkout.html'
    form_class = CheckOutForm
    model = OrderDetails
    success_url = '/checkout/ordersent'

    def form_valid(self, form):
        profile = get_object_or_404(UserProfile, user=self.request.user)
        form.instance.user_profile = profile
        self.object = form.save()

        cart = Cart(self.request)
        for unit in cart:
            UnitOrder.objects.create(
                order_id=self.object.order_key,
                item=unit['item'],
                unit_total=unit['price'],
                quantity=unit['quantity'],
                unit_size=unit['size']
                )
                
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(CheckoutFormView, self).get_context_data(**kwargs)
        cart = Cart(self.request)
        total = str(cart.unit_total())
        total = total.replace('.', '')
        total = int(total)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=total,
            currency='gbp',
            metadata={'userid': (self.request.user).id}
        )
        context['client_secret'] = intent.client_secret
        
        return context


def Ordered(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        userid = UserProfile.objects.get(user=request.user).id
        order_key = request.POST.get('order_key')
        carttotal = cart.unit_total()

        # check if the order is exists
        if OrderDetails.objects.filter(user_profile_id=userid).exists():
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
    return render(request, 'checkout/ordersent.html')
