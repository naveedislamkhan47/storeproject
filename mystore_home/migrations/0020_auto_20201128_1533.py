# Generated by Django 3.1.3 on 2020-11-28 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0019_auto_20201128_1523'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_products',
            new_name='Order_Detail',
        ),
    ]
