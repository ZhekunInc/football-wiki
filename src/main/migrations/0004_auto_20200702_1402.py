# Generated by Django 2.2.12 on 2020-07-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200630_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='place_ass',
            field=models.IntegerField(default=1, verbose_name='Place on association rating'),
        ),
        migrations.AddField(
            model_name='country',
            name='points_ass',
            field=models.IntegerField(default=1, verbose_name='Points on association rating'),
        ),
        migrations.AlterField(
            model_name='club',
            name='color1',
            field=models.CharField(blank=True, max_length=20, verbose_name='Color 1'),
        ),
        migrations.AlterField(
            model_name='club',
            name='color2',
            field=models.CharField(blank=True, max_length=20, verbose_name='Color 2'),
        ),
    ]