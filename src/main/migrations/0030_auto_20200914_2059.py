# Generated by Django 2.2.14 on 2020-09-14 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_association_ratingassociation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingassociation',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='ratingassociation',
            name='title',
        ),
    ]