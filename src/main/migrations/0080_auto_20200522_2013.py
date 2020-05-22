# Generated by Django 2.2.2 on 2020-05-22 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0079_auto_20200522_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='last',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='club', to='main.Club', verbose_name='Last winner'),
        ),
    ]