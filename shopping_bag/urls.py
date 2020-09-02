from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path(
        'add/<content_id>/', views.add_to_shopping_bag,
        name='add_to_shopping_bag'
        ),

]
