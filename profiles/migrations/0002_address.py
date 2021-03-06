# Generated by Django 3.1 on 2020-09-09 08:07

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20200908_0656'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('billing', 'Billing'), ('delivery', 'Delivery')], max_length=120)),
                ('street_address1', models.CharField(max_length=90)),
                ('street_address2', models.CharField(blank=True, max_length=90, null=True)),
                ('city', models.CharField(max_length=120)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(max_length=120)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.billing')),
            ],
        ),
    ]
