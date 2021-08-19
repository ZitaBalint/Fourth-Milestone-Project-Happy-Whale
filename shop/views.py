from django.shortcuts import get_object_or_404, render
from .models import Item, Category
# Create your views here.


def shop_items(request):
    """ Show all the products of the shop """

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, slug):
    """ Show all the products of the shop """

    item = get_object_or_404(Item, slug=slug)

    context = {
        'item': item,
    }

    return render(request, 'items/detail.html', context)
