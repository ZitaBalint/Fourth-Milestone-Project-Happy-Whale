from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import ItemForm
from .models import Category, Item

# Create your views here.


def shop_items(request):
    """ Show all the products of the shop """

    items = Item.objects.all()

    query = None

# Used Code Institute Search logic from Tutorial
    if 'query' in request.GET:
        query = request.GET['query']
        if not query:
            messages.error(request, "Please enter your search")
            return redirect(reverse('items'))
        queries = Q(name__icontains=query) | Q(item_description__icontains=query)
        items = items.filter(queries)

    context = {
        'items': items,
        'search_term': query,
    }

    return render(request, 'items/items.html', context)


def items_category(request, category_slug):
    """ shows specific category of items """

    category = get_object_or_404(Category, slug=category_slug)
    items = Item.objects.filter(category=category)

    context = {
        'category': category,
        'items': items,
        }

    return render(request, 'category/items_category.html', context)


def item_detail(request, slug):
    """ Show a specific products of the shop """

    item = get_object_or_404(Item, slug=slug)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)


def upload_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('upload_item'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ItemForm()
        
    template = 'shop/upload_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    form = ItemForm()

    context = {
        'form': form,
        'item': item,
    }

    return render(request, 'items/edit_item.html', context)


def delete_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    item.delete()

    return redirect('items.items.html')
