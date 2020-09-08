from django import forms
from .models import GuestEmail


class GuestForm(forms.ModelForm):

    class Meta:
        model = GuestEmail
        fields = ['email']

