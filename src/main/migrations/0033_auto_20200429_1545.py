# Generated by Django 3.0.5 on 2020-04-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_remove_club_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='stadium_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='stadium_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='stadium_uk',
            field=models.CharField(max_length=255, null=True),
        ),
    ]