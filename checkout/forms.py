from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'email', 'phone_number',
            'country', 'postcode', 'city', 'streetaddress',
            'house_number',)

def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes and remove auto-generated
    labels and set autofocus on first field
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'email': 'Email',
        'phone_number': 'Phone Number',
        'country': 'Country',
        'postcode': 'Postcode',
        'city': 'City',
        'streetaddress': 'Street Address',
        'house_number': 'House Number',
    }

    """
    Sets the cursor in the name field when page is loaded
    """
    self.fields['first_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholder[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].label = False
