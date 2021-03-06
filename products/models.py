from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    RATING_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    )
    name = models.CharField(max_length=250)
    brand_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    color = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    size = models.TextField(default="")
    quantity = models.IntegerField(default="")
    image_url = models.URLField(max_length=1024, null=True,
                                blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
