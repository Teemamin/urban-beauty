from django.shortcuts import render, redirect, reverse
from shopping_bag.models import Bag
from .models import Order, Billing
from profiles.models import GuestEmail
from profiles.forms import GuestForm

# Create your views here.


def checkout(request):
    bag_obj, bag_created = Bag.objects.new_or_get(request)
    order_obj = None
    # if bag_created or bag_obj.products.count() == 0:
    #     return redirect(reverse('shopping_bag')
    # else:
    # order_obj, new_order_obj = Order.objects.get_or_create(bag=bag_obj)
    user = request.user
    billing_profile = None
    form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')
    if user.is_authenticated:
        """ authenticated user checkout """
        billing_profile, billing_profile_created = \
            Billing.objects.get_or_create(
            user=user, email=user.email
            )
    elif guest_email_id is not None:
        """ guest user checkout """
        guest_email_obj = GuestEmail.objects.get(
            id=guest_email_id
            )
        billing_profile, billing_guest_profile_created = \
            Billing.objects.get_or_create(
                                        email=guest_email_obj.email)
    else:
        pass

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

