from django.shortcuts import render,redirect

# Create your views here.

from products.models import Product
from .models import Bag


def shopping_bag(request):
    bag_obj, new_obj = Bag.objects.new_or_get(request)
    # products = bag_obj.products.all()
    context = {
        'cart': bag_obj
    }
    return render(request, 'shopping_bag/shopping_bag.html', context)


def add_to_shopping_bag(request):
    product_id = request.POST.get('product_id')
    product_obj = Product.objects.get(id=product_id)
    redirect_url = request.POST.get('redirect_url')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Product not found")
            return redirect(redirect_url)
        bag_obj, new_obj = Bag.objects.new_or_get(request)
        if product_obj in bag_obj.products.all():
            bag_obj.products.remove(product_obj)
        else:
            bag_obj.products.add(product_obj)

    return redirect(redirect_url)


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
