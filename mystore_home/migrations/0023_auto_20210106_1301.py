# Generated by Django 3.1.3 on 2021-01-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0022_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pics'),
        ),
    ]