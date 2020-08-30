from django.shortcuts import render
from .models import Product, Category
# Create your views here.


def products_view(request):
    products = Product.objects.all
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)
