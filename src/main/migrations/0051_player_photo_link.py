# Generated by Django 2.2.14 on 2020-10-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_auto_20201015_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='photo_link',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Photo link'),
        ),
    ]
