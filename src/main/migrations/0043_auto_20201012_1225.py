# Generated by Django 2.2.14 on 2020-10-12 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20201008_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club', to='main.Country', verbose_name='country'),
        ),
    ]