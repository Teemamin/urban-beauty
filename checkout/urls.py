from django.urls import path
from . import views

urlpatterns = [
   path('', views.checkout, name='checkout'),
   path('payment/', views.payment_method, name='payment_method'),
   path(
    'checkout_success/', views.checkout_success,
    name='checkout_success'
    ),


]
