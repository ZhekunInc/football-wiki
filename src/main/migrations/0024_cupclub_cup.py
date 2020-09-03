# Generated by Django 2.2.14 on 2020-08-28 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_cupclub'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupclub',
            name='cup',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Cup', verbose_name='Cup'),
        ),
    ]