# Generated by Django 2.2.12 on 2020-07-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200702_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='points_ass',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Points on association rating'),
        ),
    ]
