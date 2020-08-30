from django.contrib import admin
from .models import Product, Category

# Register your models here.


class MyProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    # ordering = ('sku',)


class MyCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, MyProductAdmin)
admin.site.register(Category, MyCategoryAdmin)


# Register your models here.
