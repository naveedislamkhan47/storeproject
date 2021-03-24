# Generated by Django 3.1.3 on 2020-11-28 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0012_product_weight_grams'),
    ]

    operations = [
        migrations.AddField(
            model_name='gender_cat',
            name='slug',
            field=models.SlugField(max_length=25, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='item_cat',
            name='slug',
            field=models.SlugField(max_length=75, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_allowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='product',
            name='note',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='ranking',
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='product_cat',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_grams',
            field=models.PositiveIntegerField(verbose_name='Weight (Grams)'),
        ),
        migrations.CreateModel(
            name='Product_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50, null=True)),
                ('size', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('note', models.CharField(max_length=250, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mystore_home.product')),
            ],
        ),
    ]
