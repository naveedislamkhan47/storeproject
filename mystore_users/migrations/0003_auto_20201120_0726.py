# Generated by Django 3.1.3 on 2020-11-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore_users', '0002_auto_20201119_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Must Enter Username', max_length=254, verbose_name='email address'),
        ),
    ]
