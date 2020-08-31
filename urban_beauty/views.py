from django.shortcuts import render
from products.models import Product, Category


def home(request):
    products = Product.objects.filter(category__name="new_arrivals")
    context = {
        'products': products
    }
    return render(request, 'index.html', context)
