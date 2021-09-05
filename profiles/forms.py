from django import forms
from .models import UserProfile
# Register your models here.

# Followed Code Institute Tutorial


"""class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        placeholders = {
            'default_postcode': 'Post Code',
            'default_town_or_city': 'Town or City',
            'default_street_adress1': 'Address Line 1',
            'default_street_adress2': 'Address Line 2',
            'default_country': 'Country',
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False """
