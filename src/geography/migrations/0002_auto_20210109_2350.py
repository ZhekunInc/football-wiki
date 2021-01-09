# Generated by Django 3.0.5 on 2021-01-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(max_length=200, verbose_name='capital'),
        ),
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='flag URLs'),
        ),
    ]
