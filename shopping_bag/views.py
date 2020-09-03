from django.shortcuts import render,redirect

# Create your views here.

from products.models import Product
from .models import Bag


def shopping_bag(request):
    bag_obj, new_obj = Bag.objects.new_or_get(request)
    products = bag_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    bag_obj.total = total
    bag_obj.save()
    return render(request, 'shopping_bag/shopping_bag.html', {})


def add_to_shopping_bag(request):
    content_id = 1
    product_obj = Product.objects.get(id=content_id)
    bag_obj, new_obj = Bag.objects.new_or_get(request)
    bag_obj.products.add(product_obj)
    return redirect("")


# def shopping_bag(request):
#     return render(request, 'shopping_bag/shopping_bag.html')


# def add_to_shopping_bag(request, content_id):
#     """ """
#     number_of_product = int(request.POST.get('number_of_product'))
#     redirect_url = request.POST.get('redirect_url')
#     itm_size = None
#     if 'itm_size' in request.POST:
#         itm_size = request.POST.get('itm_size')
#     shopping_bag = request.session.get('shopping_bag', {})
#     if itm_size:
#         if content_id in list(shopping_bag.keys()):
#             shopping_bag[content_id]['itmby_size'][itm_size] += number_of_product
#         else:
#             shopping_bag[content_id]['itmby_size'][itm_size] = number_of_product
#     else:
#         if content_id in list(shopping_bag.keys()):
#             shopping_bag[content_id] += number_of_product
#         else:
#             shopping_bag[content_id] = number_of_product
#     request.session['shopping_bag'] = shopping_bag
#     print(request.session['shopping_bag'])
#     return redirect(redirect_url)
