# Generated by Django 2.2.14 on 2020-10-12 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20201012_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='league',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club', to='main.League', verbose_name='league'),
        ),
    ]
