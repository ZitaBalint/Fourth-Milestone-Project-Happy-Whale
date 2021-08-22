from django.db import models
from django.urls import reverse


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
            
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_dsiplay_name(self):
        return self.display_name


class Item(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    item_description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    review_rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.slug])

    def __str__(self):
        return self.name

