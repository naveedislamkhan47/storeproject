# Generated by Django 3.1.3 on 2020-11-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0016_auto_20201128_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='note',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]