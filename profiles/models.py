from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    default_first_name = models.CharField(max_length=50,
                                          null=True, blank=True)
    default_last_name = models.CharField(max_length=50,
                                         null=True, blank=True)
    default_email_address = models.EmailField(max_length=70,
                                              null=True, blank=True)
    default_adress_line1 = models.CharField(max_length=70,
                                            null=True, blank=True)
    default_adress_line2 = models.CharField(max_length=70,
                                            null=True, blank=True)
    default_town_or_city = models.CharField(max_length=50,
                                            null=True, blank=True)
    default_country = CountryField(max_length=10,
                                   null=True, blank=True)
    default_postcode = models.CharField(max_length=10,
                                        null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    # Followed Code INstitute tutorial
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(self, sender, instance, created, **kwargs):   
        if created:
            UserProfile.objects.create(user=instance)
        isinstance.userprofile.save()
