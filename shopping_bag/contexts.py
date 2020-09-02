from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def shopping_bag_contents(request):
    bag_content = []
    number_of_products = 0
    total_cost = 0
    shopping_bag = request.session.get('shopping_bag', {})
    for content_id, qty in shopping_bag.items():
        product = get_object_or_404(Product, pk=content_id)
        total_cost += qty * product.price
        number_of_products = qty
        bag_content.append({
            'product': product,
            'total_cost': total_cost,
            "number_of_products": number_of_products,

        })

    if total_cost < settings.FREE_DELIVERY:
        delivery_cost = total_cost * Decimal(settings.DELIVERY_PERCENT / 100)
        get_free_delivery = settings.FREE_DELIVERY - total_cost
    else:
        delivery_cost = 0
        get_free_delivery = 0

    grand_total = total_cost + delivery_cost

    context = {
        'bag_content': bag_content,
        'number_of_products': number_of_products,
        'total_cost': total_cost,
        'delivery_cost': delivery_cost,
        'get_free_delivery': get_free_delivery,
        'grand_total': grand_total,
        'free_delivery': settings.FREE_DELIVERY

    }
    return context
