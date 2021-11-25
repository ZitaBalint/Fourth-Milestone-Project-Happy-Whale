from django.contrib import messages
from django.shortcuts import get_object_or_404, render

from shop_checkout.models import OrderDetails

from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.
# Followed Code institute tutorial


def Profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')

    form = UserProfileForm(instance=profile)
    orders = OrderDetails.objects.filter(user=request.user)

    template = 'profile/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

    