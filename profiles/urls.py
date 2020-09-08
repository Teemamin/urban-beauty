from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_profile, name='guest_profile'),

]
