# Generated by Django 2.2.11 on 2021-01-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag_file',
            field=models.ImageField(blank=True, help_text='Recomended size 512x512px', null=True, upload_to='images/geo/flags', verbose_name='Flag'),
        ),
    ]
