import uuid
from django.db import models
from django.db.models.signals import post_save, pre_save
import math

from shopping_bag.models import Bag
from django.contrib.auth.models import User

# Create your models here.


class Billing(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
        )
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        Billing.objects.get_or_create(user=instance, email=instance.email)


post_save.connect(user_created_receiver, sender=User)




ORDER_STATUS = (
    ('created', 'Created'),
    ('paid', 'Paid'),
)


class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, bag_obj):
        created = False
        qs = self.get_queryset().filter(
                billing_profile=billing_profile,
                bag=bag_obj,
                active=True)
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(
                    billing_profile=billing_profile,
                    bag=bag_obj
                    )
            created = True
        return obj, created




class Order(models.Model):
    billing_profile = models.ForeignKey(Billing, null=True, blank=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=50, default='created', choices=ORDER_STATUS
        )
    delivery_total = models.DecimalField(
        default=5.88, max_digits=100, decimal_places=2
        )
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        bag_total = self.bag.total
        delivery_total = self.delivery_total
        grand_total = math.fsum([bag_total, delivery_total])
        total_formated = format(grand_total, '.2f')
        self.total = total_formated
        self.save()
        return total_formated
    

    def save(self, *args, **kwargs):
        """
        Set the order number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    objects = OrderManager()


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    qs = Order.objects.filter(bag=instance.bag).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)


pre_save.connect(pre_save_create_order_id, sender=Order)

def post_save_bag_total(sender, instance, created, *args, **kwargs):
    if not created:
        bag_obj = instance
        bag_total = bag_obj.total
        bag_id = bag_obj.id
        queryset = Order.objects.filter(bag__id=bag_id)
        if queryset.count() == 1:
            order_obj = queryset.first()
            order_obj.update_total()


post_save.connect(post_save_bag_total, sender=Bag)


def post_save_bag_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()


post_save.connect(post_save_bag_order, sender=Order)



