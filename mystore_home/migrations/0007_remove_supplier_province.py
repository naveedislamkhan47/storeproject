# Generated by Django 3.1.3 on 2020-11-21 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_home', '0006_auto_20201121_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='province',
        ),
    ]
