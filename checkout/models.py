import uuid
from django.db import models
from django.db.models.signals import post_save
from decimal import Decimal

from shopping_bag.models import Bag

# Create your models here.

ORDER_STATUS = (
    ('created', 'Created'),
    ('paid', 'Paid'),
)


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=50, default='created', choices=ORDER_STATUS
        )
    delivery_total = models.DecimalField(
        default=5.88, max_digits=100, decimal_places=2
        )
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        bag_total = self.bag.total
        delivery_total = self.delivery_total
        grand_total = Decimal(bag_total) + Decimal(delivery_total) 
        self.total = grand_total
        self.save()
        return grand_total

    def save(self, *args, **kwargs):
        """
        Set the order number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


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
