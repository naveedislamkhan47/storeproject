# Generated by Django 3.1.3 on 2020-11-21 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0007_remove_supplier_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping_address',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystore_home.order'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('CR', 'Credit Card'), ('DR', 'Debit Card'), ('COD', 'Cash On Delivery')], max_length=3),
        ),
    ]
