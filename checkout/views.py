from django.shortcuts import render, redirect, reverse
from shopping_bag.models import Bag
from .models import Order, Billing
from profiles.models import GuestEmail, Address
from profiles.forms import GuestForm, AddressForm

# Create your views here.


def checkout(request):
    bag_obj, bag_created = Bag.objects.new_or_get(request)
    order_obj = None
    if bag_created or bag_obj.products.count() == 0:
        return redirect('shopping_bag')

    form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    delivery_address_id = request.session.get("delivery_address_id", None)
    billing_profile, billing_profile_created = \
        Billing.objects.new_or_get(request)
    address_queryset = None

    if billing_profile is not None:
        if request.user.is_authenticated:
            address_queryset = Address.objects.filter(
                billing_profile=billing_profile
                )
        order_obj, order_obj_created = Order.objects.new_or_get(
            billing_profile, bag_obj
            )
        if delivery_address_id:
            order_obj.delivery_address = Address.objects.get(
                id=delivery_address_id
                )
            del request.session["delivery_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(
                id=billing_address_id
                )
            del request.session["billing_address_id"]
        if billing_address_id or delivery_address_id:
            order_obj.save()

    if request.method == "POST":
        """see if order is done"""
        is_done = order_obj.see_if_order_done()
        if is_done:
            order_obj.mark_as_paid()
            # request.session['bag_items'] = 0
            del request.session['bag_id']
            return redirect("/checkout/success")

    context = {
        'order': order_obj,
        'billing': billing_profile,
        'form': form,
        'address_form': address_form,
        'address_queryset': address_queryset,
        'bag_obj': bag_obj,
    }
    return render(request, 'checkout/checkout.html', context)

def checkout_success(request):
    return render(request, 'checkout/checkout_success.html')

