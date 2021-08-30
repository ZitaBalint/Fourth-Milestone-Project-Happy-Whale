from django.db import models
import uuid
from shop.models import Item

# Create your models here.

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class OrderDetails(models.Model):
    order_number = models.CharField(max_length=15, null=False, editable=False)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField
    adress_line1 = models.CharField(max_length=70, null=False, blank=False)
    adress_line1 = models.CharField(max_length=70, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=70, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    unit_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        geterate order number
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class ItemOrder(models.Model):
    order = models.ForeignKey(OrderDetails, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    item_size = models.CharField(max_length=20, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def __str__(self):
        return f'slug {self.item.sku} on order {self.order.order_number}'