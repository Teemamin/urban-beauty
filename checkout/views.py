from django.shortcuts import render, redirect, reverse
from shopping_bag.models import Bag
from .models import Order

# Create your views here.


def checkout(request):
    bag_obj, bag_created = Bag.objects.new_or_get(request)
    #order_obj = None
    # if bag_created or bag_obj.products.count() == 0:
    #     return redirect(reverse('shopping_bag')
    # else:
    order_obj, new_order_obj = Order.objects.get_or_create(bag=bag_obj)
    
    context = {
        'order': order_obj,
    }
    return render(request, 'checkout/checkout.html', context)
