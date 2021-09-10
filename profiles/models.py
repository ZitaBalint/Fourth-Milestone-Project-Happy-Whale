from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
 # Followed Code INstitute tutorial

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_address_line1 = models.CharField(max_length=70,
                                            null=True, blank=True)
    default_address_line2 = models.CharField(max_length=70,
                                            null=True, blank=True)
    default_town_or_city = models.CharField(max_length=50,
                                            null=True, blank=True)
    default_country = CountryField(max_length=10,
                                   null=True, blank_label='Country',
                                   blank=True)
    default_postcode = models.CharField(max_length=10,
                                        null=True, blank=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.user.username
   
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()
