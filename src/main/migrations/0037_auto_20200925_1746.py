# Generated by Django 2.2.14 on 2020-09-25 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20200925_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='rating',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.RatingAssociation', verbose_name='Rating Associations'),
        ),
    ]
