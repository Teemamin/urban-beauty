from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed
from products.models import Product


# Create your models here.
User = settings.AUTH_USER_MODEL


class BagManager(models.Manager):
    def new_or_get(self, request):
        bag_id = request.session.get("bag_id", None)
        qs = self.get_queryset().filter(id=bag_id)
        if qs.count() == 1:
            new_obj = False
            bag_obj = qs.first()
            if request.user.is_authenticated and bag_obj.user is None:
                bag_obj.user = request.user
                bag_obj.save()
        else:
            bag_obj = Bag.objects.new(user=request.user)
            new_obj = True
            request.session['bag_id'] = bag_obj.id
        return bag_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Bag(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2
    )
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = BagManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_bag_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove'\
         or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_bag_receiver, sender=Bag.products.through)


def pre_save_bag_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = float(instance.subtotal) * float(1.08)
    else:
        instance.total = 0.00


pre_save.connect(pre_save_bag_receiver, sender=Bag)
