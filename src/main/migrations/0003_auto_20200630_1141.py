# Generated by Django 2.2.12 on 2020-06-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='color1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='club',
            name='color2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
