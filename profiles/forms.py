from django import forms
from .models import GuestEmail, Address


class GuestForm(forms.ModelForm):

    class Meta:
        model = GuestEmail
        fields = ['email']


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = [
                'street_address1',
                'street_address2',
                'city',
                'state',
                'postcode',
                'country',
        ]

