from django.contrib import admin
from .models import OrderDetails, UnitOrder

# Register your models here.


class UnitOrderAdminInline(admin.TabularInline):
    model = UnitOrder
    readonly_fields = ('unit_total',)

# The basic followed by Code Institute tutorial


class OrderAdmin(admin.ModelAdmin):
    inlines = (UnitOrderAdminInline,)

    readonly_fields = ('order_number', 'date', 'unit_total',)

    fields = ('order_number', 'date', 'first_name', 'last_name',
              'email_address', 'adress_line1',
              'adress_line2', 'postcode', 'town_or_city',
              'country', 'unit_total',)

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'unit_total',)

    ordering = ('-date',)


admin.site.register(OrderDetails, OrderAdmin)
