# Generated by Django 2.2.2 on 2020-05-22 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0069_auto_20200522_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='last',
        ),
    ]