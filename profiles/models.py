from django.db import models
from django_countries.fields import CountryField



# Create your models here.


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('delivery', 'Delivery'),
)


class Address(models.Model):
    billing_profile = models.ForeignKey('checkout.Billing', on_delete=models.CASCADE)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    street_address1 = models.CharField(max_length=90, null=False, blank=False)
    street_address2 = models.CharField(max_length=90, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = CountryField(null=False, blank=False)
    state = models.CharField(max_length=120)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.billing_profile)
