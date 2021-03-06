# Generated by Django 2.2.14 on 2020-09-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20200914_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association',
            name='cl_teams',
        ),
        migrations.RemoveField(
            model_name='association',
            name='el_teams',
        ),
        migrations.AddField(
            model_name='association',
            name='place',
            field=models.IntegerField(blank=True, default=1, verbose_name='Place'),
        ),
        migrations.AddField(
            model_name='association',
            name='point_year1',
            field=models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=7, verbose_name='Points on association rating'),
        ),
        migrations.AddField(
            model_name='association',
            name='point_year2',
            field=models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=7, verbose_name='Points on association rating'),
        ),
        migrations.AddField(
            model_name='association',
            name='point_year3',
            field=models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=7, verbose_name='Points on association rating'),
        ),
        migrations.AddField(
            model_name='association',
            name='point_year4',
            field=models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=7, verbose_name='Points on association rating'),
        ),
        migrations.AddField(
            model_name='association',
            name='point_year5',
            field=models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=7, verbose_name='Points on association rating'),
        ),
        migrations.AddField(
            model_name='association',
            name='teams',
            field=models.IntegerField(blank=True, default=0, verbose_name='The number of represented Euro Cups'),
        ),
    ]
