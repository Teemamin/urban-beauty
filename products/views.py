from django.shortcuts import render, get_object_or_404,\
    redirect, reverse
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm
# from .filters import ProductFilter
# Create your views here.


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all
    # myFilter = ProductFilter(request.GET, queryset=products)
    # products = myFilter.qs
    if request.GET:
        if 'cat' in request.GET:
            categories = request.GET['cat'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'search' in request.GET:
            search_word = request.GET['search']
            if not search_word:
                messages.error(request, "please enter a message")
                return redirect(reverse('products'))
            search_words = Q(name__icontains=search_word) |\
                Q(description__icontains=search_word)\
                | Q(color__icontains=search_word)
            products = products.filter(search_words)
    context = {
        'products': products,
        'categories': categories,
        # 'myFilter': myFilter
    }
    return render(request, 'products/products.html', context)


def single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/single_product.html', context)


def new_product(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/new_product.html', context)
