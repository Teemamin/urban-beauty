from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse
from .models import GuestEmail, Address
from .forms import GuestForm, AddressForm
from checkout.models import Billing

# Create your views here.


def guest_profile(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    # next_ = request.GET.get('next')
    # next_post = request.POST.get('next')
    redirect_path = request.POST.get('redirect_url')
    if form.is_valid():
        email = form.save()
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("accounts/account_signup")
    return redirect("accounts/account_signup")


def checkout_address_create(request):
    form = AddressForm(request.POST or None)
    context = {
        "form": form
    }

    redirect_path = request.POST.get('redirect_url')
    if form.is_valid():
        print(request.POST)
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = Billing.objects.new_or_get(request)
        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'delivery')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()
            request.session[address_type + "_address_id"] = instance.id
            print(address_type + "_address_id")
        else:
            print("Error")
            return redirect(redirect_path)

    return redirect(redirect_path) 