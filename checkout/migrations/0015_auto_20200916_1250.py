# Generated by Django 3.1 on 2020-09-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_auto_20200916_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_total',
            field=models.DecimalField(decimal_places=2, default=5.88, max_digits=100),
        ),
    ]
