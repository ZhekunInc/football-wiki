# Generated by Django 2.2.12 on 2020-06-30 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Color', models.CharField(max_length=20)),
                ('name', models.ForeignKey(default='color', on_delete=django.db.models.deletion.CASCADE, to='main.Club', verbose_name='Club')),
            ],
            options={
                'verbose_name': 'Color',
            },
        ),
    ]
