# Generated by Django 3.0.5 on 2020-05-22 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0084_auto_20200522_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='main_text',
        ),
        migrations.RemoveField(
            model_name='league',
            name='main_text_en',
        ),
        migrations.RemoveField(
            model_name='league',
            name='main_text_ru',
        ),
        migrations.RemoveField(
            model_name='league',
            name='main_text_uk',
        ),
    ]