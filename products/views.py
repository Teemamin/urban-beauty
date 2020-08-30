from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.


def all_products(request):
    products = Product.objects.all
    categories = Category.objects.all
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/products.html', context)


def single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/single_product.html', context)
