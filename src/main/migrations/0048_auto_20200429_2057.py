# Generated by Django 3.0.5 on 2020-04-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20200429_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='kits',
            name='title_en',
            field=models.CharField(default='Kits', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='kits',
            name='title_ru',
            field=models.CharField(default='Kits', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='kits',
            name='title_uk',
            field=models.CharField(default='Kits', max_length=200, null=True),
        ),
    ]
