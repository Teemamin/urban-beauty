from django.shortcuts import render, redirect, reverse
from shopping_bag.models import Bag
from .models import Order, Billing
from profiles.models import GuestEmail
from profiles.forms import GuestForm

# Create your views here.


def checkout(request):
    bag_obj, bag_created = Bag.objects.new_or_get(request)
    order_obj = None
    if bag_created or bag_obj.products.count() == 0:
        return redirect('shopping_bag')
    
    form = GuestForm()
    billing_profile, billing_profile_created = \
        Billing.objects.new_or_get(request)

    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(
            billing_profile, bag_obj
            )

    context = {
        'order': order_obj,
        'billing': billing_profile,
        'form': form,
    }
    return render(request, 'checkout/checkout.html', context)

