from django.shortcuts import render
from . models import UserProfile
from . forms import UserProfileForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from shop_checkout.models import OrderDetails
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
    orders = profile.orders.all()

    template = 'profile/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_key):
    user_id = request.user.username
    orders = OrderDetails.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
    