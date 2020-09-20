from django.shortcuts import render,redirect, get_object_or_404, reverse, HttpResponse

# Create your views here.

from products.models import Product
from .models import Bag, OrderLineItem


def shopping_bag(request):
    bag_obj, new_obj = Bag.objects.new_or_get(request)
    # products = bag_obj.products.all()
    context = {
        'cart': bag_obj
    }
    return render(request, 'shopping_bag/shopping_bag.html', context)


def add_to_shopping_bag(request):
    product_id = request.POST.get('product_id')
    # product_obj = Product.objects.get(pk=product_id)

    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'itm_size' in request.POST:
        size = request.POST['itm_size']
    print(size)

    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
            product_obj.size = size
            print(size)
            print(product_obj)
        except Product.DoesNotExist:
            print("Product not found")
            return redirect(redirect_url)
        bag_obj, new_obj = Bag.objects.new_or_get(request)
    

        #print(bag_obj.products.all())
        # if size == bag_obj.products.all():
        #     quantity += product_obj
        #     bag_obj.products.add(product_obj, quantity)
        # else:
        #     bag_obj.products.add(product_obj)
        if bag_obj.order_line_items.filter(product=product_obj):
            # bag_obj.products.remove(product_obj)
            print('hahaha here..')
            bag_prod_objs = bag_obj.order_line_items.filter(product=product_obj, product_size=size)
            print(bag_prod_objs)
            if bag_prod_objs:
                bag_prod_obj = bag_prod_objs[0]
                if bag_prod_obj.product_size == size:
                    bag_prod_obj.quantity += quantity
                    bag_prod_obj.save()
            else:
                bag_obj.order_line_items.create(product=product_obj, product_size = size, quantity=quantity)
        else:
            bag_obj.order_line_items.create(product=product_obj, product_size = size, quantity=quantity)

    return redirect(redirect_url)


def remove_from_bag(request, product_id):
    product_obj = get_object_or_404(OrderLineItem, pk=product_id)
    print(product_obj)
    redirect_url = request.POST.get('redirect_url')
    bag_obj, new_obj = Bag.objects.new_or_get(request)
    
    # if product_obj in bag_obj.order_line_items.all():
    bag_obj.order_line_items.remove(product_obj)
    print(redirect_url)
    return redirect('shopping_bag')

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
