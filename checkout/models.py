from django.db import models
import uuid
from shopping_bag.models import Bag

# Create your models here.

ORDER_STATUS = (
    ('created', 'Created'),
    ('paid', 'Paid'),
)


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    bag = models.ForeignKey(Bag)
    order_status = models.CharField(
        max_length=50, default='created', choices=ORDER_STATUS
        )
    delivery_total = models.DecimalField(
        default=5.00, max_digits=100, decimal_places=2
        )
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.order_number
