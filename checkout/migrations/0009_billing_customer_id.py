# Generated by Django 3.1 on 2020-09-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20200910_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='customer_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
