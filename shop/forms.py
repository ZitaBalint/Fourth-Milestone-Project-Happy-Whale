from django import forms
from .models import Category, Item

# followed the Code Institute turorial

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            categories = Category.object.all()
            names = [(c.id, c.get_absolute_url()) for c in categories]

            self.fields['category'].choices = names
            for field_name, field in self.fields.items():
                filed.widget.attrs['class'] = 'border-black rounded-0'