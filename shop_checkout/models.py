from django.db import models
from django_countries.fields import CountryField

from profiles.models import UserProfile
from shop.models import Item

# Create your models here.
# Followed the Code Institute Tutorial

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class OrderDetails(models.Model):

    order_key = models.CharField(max_length=200, null=False, editable=False, default=1)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(default='email address')
    address_line1 = models.CharField(max_length=70, blank=False)
    address_line2 = models.CharField(max_length=70, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    country = CountryField(default='Select Country')
    postcode = models.CharField(max_length=10, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    unit_total = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=False, default=0)
    billing_status = models.BooleanField(default=False)
    objects = models.Manager()

    class Meta:
        ordering = ('-date_created',)
    
    def __str__(self):
        return str(self.date_created)


class UnitOrder(models.Model):
    order = models.ForeignKey(OrderDetails, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='units')
    item = models.ForeignKey(Item, related_name='order_units',
                             on_delete=models.CASCADE, default=1)
    unit_size = models.CharField(max_length=20, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    unit_total = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=False, blank=False, editable=False)
    objects = models.Manager()

    def __str__(self):
        return str(self.id)
