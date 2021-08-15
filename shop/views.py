from django.shortcuts import render
from .models import Item
# Create your views here.


def shop_items(request):
    """ Show all the products of the shop """

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'items/items.html', context)
