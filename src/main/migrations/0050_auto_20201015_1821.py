# Generated by Django 2.2.14 on 2020-10-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_auto_20201015_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fifacountry',
            name='continent',
        ),
        migrations.AlterField(
            model_name='fifacountry',
            name='points',
            field=models.IntegerField(blank=True, null=True, verbose_name='Points on association rating'),
        ),
    ]
