# Generated by Django 3.0.5 on 2020-04-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20200429_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='nickname_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='nickname_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='nickname_uk',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='short_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='short_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='short_name_uk',
            field=models.CharField(max_length=255, null=True),
        ),
    ]