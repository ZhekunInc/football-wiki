# Generated by Django 2.2.14 on 2020-08-28 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_countryplayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryplayer',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Country', verbose_name='Country'),
        ),
    ]
