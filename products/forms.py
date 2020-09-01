from django import forms
from .models import Product
from crispy_forms.helper import FormHelper


class ProductForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
    class Meta:
        model = Product
        fields = '__all__'

