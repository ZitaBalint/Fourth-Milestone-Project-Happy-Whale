from django.contrib import admin
from .models import OrderDetails, ItemOrder

# Register your models here.


class ItemOrderAdminInline(admin.TabularInline):
    model = ItemOrder
    readonly_fields = ('item_total',)

# The basic followed by Code Institute tutorial


class OrderAdmin(admin.ModelAdmin):
    inlines = (ItemOrderAdminInline,)

    readonly_fields = ('order_number', 'date', 'unit_total',)

    fields = ('order_number', 'date', 'first_name', 'last_name',
              'email_address', 'adress_line1',
              'adress_line2', 'postcode', 'town_or_city',
              'country', 'unit_total',)

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'unit_total',)

    ordering = ('-date',)


admin.site.register(OrderDetails, OrderAdmin)
