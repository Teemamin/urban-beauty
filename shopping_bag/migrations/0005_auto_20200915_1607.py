# Generated by Django 3.1 on 2020-09-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200915_1607'),
        ('shopping_bag', '0004_auto_20200915_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
        migrations.DeleteModel(
            name='BagItem',
        ),
    ]
