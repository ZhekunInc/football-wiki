# Generated by Django 3.0.5 on 2020-04-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200412_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='picture',
            field=models.ImageField(blank=True, help_text='Recomended size 512x512px', null=True, upload_to='src/main/static/images/country/', verbose_name='Image'),
        ),
    ]
