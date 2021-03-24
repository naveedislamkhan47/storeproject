# Generated by Django 3.1.3 on 2020-11-21 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mystore_home', '0002_delete_prod_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender_Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mystore_home.gender_cat')),
            ],
        ),
        migrations.CreateModel(
            name='Item_Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('product_cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mystore_home.product_cat')),
            ],
        ),
    ]