from django.contrib import admin
from .models import Item, Category


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'item_code',
        'name',
        'category',
        'price',
        'review_rating',
        'image_url',
    )

    ordering = ('item_code', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
