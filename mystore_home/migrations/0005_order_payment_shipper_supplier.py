# Generated by Django 3.1.3 on 2020-11-21 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0004_customer_shipping_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('CR', 'Credit Card'), ('Dr', 'Debit Card'), ('COD', 'Cash On Delivery')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('branch', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
                ('contact_person_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('phone', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('province', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=250)),
                ('type_of_goods', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('fullfilled', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystore_home.customer')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystore_home.payment')),
                ('shipper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystore_home.shipper')),
            ],
        ),
    ]
