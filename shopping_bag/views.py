from django.shortcuts import render,redirect

# Create your views here.


def shopping_bag(request):
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, content_id):
    """ """
    number_of_product = int(request.POST.get('number_of_product'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if content_id in list(shopping_bag.keys()):
        shopping_bag[content_id] += number_of_product
    else:
        shopping_bag[content_id] = number_of_product
    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(redirect_url)
