from django.contrib import admin

# Register your models here.
from .models import Order, Billing

admin.site.register(Order)
admin.site.register(Billing)

