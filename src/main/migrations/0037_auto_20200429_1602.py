# Generated by Django 3.0.5 on 2020-04-29 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20200429_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='continent',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='continent',
            name='slug_ru',
        ),
        migrations.RemoveField(
            model_name='continent',
            name='slug_uk',
        ),
    ]
