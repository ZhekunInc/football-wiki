# Generated by Django 3.0.5 on 2020-04-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20200429_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, help_text='Recomended size 512x512px', null=True, upload_to='images/player', verbose_name='Image'),
        ),
    ]
