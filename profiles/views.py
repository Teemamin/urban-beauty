from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import HttpResponse
from .models import GuestEmail
from .forms import GuestForm

# Create your views here.


def guest_profile(request):
    form = GuestForm(request.POST or None)
    context = {
        "form": form
    }
    # next_ = request.GET.get('next')
    # next_post = request.POST.get('next')
    redirect_path = request.POST.get('redirect_url') # next_ or next_post or None
    if form.is_valid():
        email = form.save()
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("accounts/account_signup")
    return redirect("accounts/account_signup")
