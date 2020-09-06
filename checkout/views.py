from django.shortcuts import render, redirect, reverse
from shopping_bag.models import Bag
from .models import Order, Billing

# Create your views here.


def checkout(request):
    bag_obj, bag_created = Bag.objects.new_or_get(request)
    # order_obj = None
    # if bag_created or bag_obj.products.count() == 0:
    #     return redirect(reverse('shopping_bag')
    # else:
    order_obj, new_order_obj = Order.objects.get_or_create(bag=bag_obj)
    user = request.user
    billing = None
    if user.is_authenticated:
        billing, billing_profile_created = Billing.objects.get_or_create(
            user=user, email=user.email
            )
    context = {
        'order': order_obj,
        'billing': billing,
    }
    return render(request, 'checkout/checkout.html', context)
