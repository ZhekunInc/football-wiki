# Generated by Django 2.2.12 on 2020-07-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200702_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='cl_teams',
            field=models.IntegerField(default=0, verbose_name='The number of represented in the Champions League'),
        ),
        migrations.AlterField(
            model_name='country',
            name='points_ass',
            field=models.IntegerField(default=0, verbose_name='Points on association rating'),
        ),
    ]
