# Generated by Django 3.1.3 on 2021-01-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0021_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='pics'),
        ),
    ]