# Generated by Django 3.1.3 on 2020-11-29 04:03

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0020_auto_20201128_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None),
            preserve_default=False,
        ),
    ]