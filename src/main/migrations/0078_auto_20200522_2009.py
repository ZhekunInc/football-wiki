# Generated by Django 2.2.2 on 2020-05-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0077_auto_20200522_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='main_text_en',
        ),
        migrations.RemoveField(
            model_name='country',
            name='main_text_ru',
        ),
        migrations.RemoveField(
            model_name='country',
            name='main_text_uk',
        ),
        migrations.RemoveField(
            model_name='country',
            name='president_en',
        ),
        migrations.RemoveField(
            model_name='country',
            name='president_ru',
        ),
        migrations.RemoveField(
            model_name='country',
            name='president_uk',
        ),
        migrations.RemoveField(
            model_name='league',
            name='count_team',
        ),
        migrations.RemoveField(
            model_name='league',
            name='founded',
        ),
        migrations.RemoveField(
            model_name='league',
            name='last',
        ),
        migrations.RemoveField(
            model_name='league',
            name='main_text',
        ),
        migrations.RemoveField(
            model_name='league',
            name='website',
        ),
    ]