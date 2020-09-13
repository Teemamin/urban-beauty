from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.single_product,
         name='single_product'),
    path('new/', views.new_product, name='new_product'),

]
