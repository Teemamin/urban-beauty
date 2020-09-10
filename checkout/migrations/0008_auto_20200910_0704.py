# Generated by Django 3.1 on 2020-09-10 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_address'),
        ('checkout', '0007_auto_20200908_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='profiles.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address', to='profiles.address'),
        ),
    ]
