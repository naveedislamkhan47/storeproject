# Generated by Django 3.1.3 on 2020-11-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0009_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]