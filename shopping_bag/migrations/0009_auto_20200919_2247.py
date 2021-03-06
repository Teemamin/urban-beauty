# Generated by Django 3.1 on 2020-09-19 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200919_2228'),
        ('shopping_bag', '0008_auto_20200919_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bag',
            name='products',
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_size', models.CharField(blank=True, max_length=2, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='bag',
            name='order_line_item',
            field=models.ManyToManyField(blank=True, to='shopping_bag.OrderLineItem'),
        ),
    ]
