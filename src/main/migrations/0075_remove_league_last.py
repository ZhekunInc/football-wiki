# Generated by Django 2.2.2 on 2020-05-22 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0074_auto_20200522_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='last',
        ),
    ]